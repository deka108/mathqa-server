# from drf_haystack.viewsets import HaystackViewSet
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view

from apiv2.search.fsearch import formula_indexer as fi, formula_retriever as\
    fr, formula_transformer as ft, formula_clustering as fc
from apiv2.serializers import *
from apiv2.permissions import *

import logging

logger = logging.getLogger(__name__)

schema_view = get_schema_view(title='MathQA API')


class EducationLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
    permission_classes = (permissions.AllowAny,)


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('education_level',)
    # def get_queryset(self):
    #     try:
    #         education_level = EducationLevel.objects.get(pk=self.kwargs.get(
    #             'education_level_id'))
    #         return self.queryset.filter(education_level=education_level)
    #     except EducationLevel.DoesNotExist:
    #         education_level = None
    #     return self.queryset


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('subject',)


class ConceptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('topic',)


class SubconceptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subconcept.objects.all()
    serializer_class = SubconceptSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept',)


class PapersetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paperset.objects.all()
    serializer_class = PapersetSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('subject',)


class PaperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('paperset',)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'subconcept', 'paper', 'keypoints',
                     'keywords', 'keywords')


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('question')


class FormulaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'question')


class FormulaIndexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FormulaIndex.objects.all()
    serializer_class = FormulaIndexSerializer
    permission_classes = (permissions.AllowAny,)


class KeyPointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = KeyPoint.objects.all()
    serializer_class = KeyPointSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'question')


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'question')


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def reindex_all_formula(request):
    user = request.data["username"]
    pw = request.data["password"]

    if user == "admin" and pw == "123456":
        try:
            fi.reindex_all_formulas()
            return Response("Formula and formula index table has been " +
                            "reindexed successfully.")
        except Exception:
            return Response("Unable to reindex the formula and formula index" +
                            "table.")

    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")

# class TopicList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = TopicSerializer
#
#     def get_queryset(self):
#         queryset = Topic.objects.all()
#         subj_id = self.kwargs.get('subj_id')
#         if subj_id is not None:
#             queryset = queryset.filter(subject=subj_id)
#         return queryset
#
#
# class TopicDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Topic.objects.all()
#     serializer_class = TopicSerializer
#
#
# class ConceptList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = ConceptSerializer
#
#     def get_queryset(self):
#         queryset = Concept.objects.all()
#         subj_id = self.kwargs.get('subj_id')
#         topic_id = self.kwargs.get('topic_id')
#         if subj_id is not None:
#             queryset = queryset.filter(
#                 topic__in=Topic.objects.filter(subject=subj_id))
#         elif topic_id is not None:
#             queryset = queryset.filter(topic=topic_id)
#
#         return queryset
#
#
#
#
# class QuestionList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = QuestionSerializer
#
#     def get_queryset(self):
#         queryset = Question.objects.all()
#         subj_id = self.kwargs.get('subj_id')
#         topic_id = self.kwargs.get('topic_id')
#         concept_id = self.kwargs.get('concept_id')
#
#         if "sample" in self.request.path:
#             queryset = queryset.filter(keypoint__isnull=False)
#         elif "real" in self.request.path:
#             queryset = queryset.filter(keypoint__isnull=True)
#
#         if subj_id is not None:
#             queryset = queryset.filter(concept__in=Concept.objects.filter(
#                 topic__in=Topic.objects.filter(subject=subj_id)))
#         elif topic_id is not None:
#             queryset = queryset.filter(
#                 concept__in=Concept.objects.filter(topic=topic_id))
#         elif concept_id is not None:
#             queryset = queryset.filter(concept=concept_id)
#
#         return queryset

# class KeyPointList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = KeyPointSerializer
#
#     def get_queryset(self):
#         queryset = KeyPoint.objects.all()
#         concept_id = self.kwargs.get('concept_id')
#
#         if concept_id is not None:
#             queryset = queryset.filter(concept=concept_id)
#
#         return queryset
#
#
#
# class FormulaIndexList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = FormulaIndex.objects.all()
#     serializer_class = FormulaIndexSerializer
#     print(FormulaIndex.objects.count())
#
#
#
#
# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def search_text_db(request):
#     if request.method == 'GET':
#         return Response({"message": "Hello, world!"})
#     elif request.method == 'POST':
#         query = request.data["data"]
#         queryset = Question.objects.filter(content__icontains=query)
#         serializer = QuestionSerializer(queryset,
#                                         context={'request': request},
#                                         many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def search_formula(request):
#     if request.method == 'GET':
#         return Response({"content":"x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}."})
#     elif request.method == 'POST':
#         query = request.data["content"]
#         questions = fr.search_formula(query)
#         serializer = QuestionSerializer(questions,
#                                         context={'request': request},
#                                         many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def search_formula_cluster(request):
#     if request.method == 'GET':
#         data = ft.transform_formulas()
#         return Response(data)
#     elif request.method == 'POST':
#         query = request.data["content"]
#         data = fc.generate_kmeans_cluster(query)
#         return Response(data)


# class QuestionSearchView(HaystackViewSet):
#     index_models = [Question]
#     serializer_class = QuestionHaystackSerializer