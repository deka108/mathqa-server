import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view

from apiv2.permissions import *
from apiv2.search.fsearch import formula_indexer as fi, formula_retriever as\
    fr
from apiv2.serializers_hyperlink import *

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
                     'keywords')


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('question',)


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


class TestFormulaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestFormula.objects.all()
    serializer_class = TestFormulaSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'question')


class TestFormulaIndexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestFormulaIndex.objects.all()
    serializer_class = TestFormulaIndexSerializer
    permission_classes = (permissions.AllowAny,)


class KeyPointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = KeyPoint.objects.all()
    serializer_class = KeyPointSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'question', 'type')


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'question')


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def reindex_all_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        try:
            fi.reindex_all_formulas(reset_formula=True)
            return Response("Formula and formula index table has been " +
                            "reindexed successfully.")
        except Exception as e:
            print(e)
            return Response("Unable to reindex the formula and formula index" +
                            " table.")
    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_text_db(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    elif request.method == 'POST':
        query = request.data["data"]
        queryset = Question.objects.filter(content__icontains=query)
        serializer = QuestionSerializer(queryset,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_formula(request):
    if request.method == 'GET':
        return Response({"content":"x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}."})
    elif request.method == 'POST':
        query = request.data.get("content")
        questions = fr.search_formula(query)
        serializer = QuestionSerializer(questions,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)

# class QuestionSearchView(HaystackViewSet):
#     index_models = [Question]
#     serializer_class = QuestionHaystackSerializer