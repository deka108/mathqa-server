# # from drf_haystack.viewsets import HaystackViewSet
# from rest_framework import generics
# from rest_framework import viewsets
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
#
# from apiv2.models import *
# from search import formula_indexer as fi
# from search import formula_retriever as fr
# from search import formula_transformer as ft
# from search import formula_clustering as fc
# from .serializers import *
# from .permissions import *
#
# import logging
#
# logger = logging.getLogger(__name__)
#
#
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
# class ConceptDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Concept.objects.all()
#     serializer_class = ConceptSerializer
#
#
# class PaperList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Paper.objects.all()
#     serializer_class = PaperSerializer
#
#
# class PaperDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Paper.objects.all()
#     serializer_class = PaperSerializer
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
#
#
# class QuestionDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#
# class AnswerPartList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = AnswerPart.objects.all()
#     serializer_class = AnswerPartSerializer
#
#
# class AnswerPartDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = AnswerPart.objects.all()
#     serializer_class = AnswerPartSerializer
#
#
# class SubjectList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
#
# class SubjectDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
#
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
# class KeyPointDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = KeyPoint.objects.all()
#     serializer_class = KeyPointSerializer
#
#
# class FormulaList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Formula.objects.all()
#     serializer_class = FormulaSerializer
#
#
# class FormulaDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Formula.objects.all()
#     serializer_class = FormulaSerializer
#
#
# class FormulaIndexList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = FormulaIndex.objects.all()
#     serializer_class = FormulaIndexSerializer
#     print(FormulaIndex.objects.count())
#
#
# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
# def reindex_all_formula(request):
#     fi.reindex_all_formulas()
#     return Response("Formula and formula index table has been reindexed "
#                         "successfully.")
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
#
#
# # class QuestionSearchView(HaystackViewSet):
# #     index_models = [Question]
# #     serializer_class = QuestionHaystackSerializer