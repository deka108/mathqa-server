# from drf_haystack.viewsets import HaystackViewSet
# from django_filters.rest_framework import DjangoFilterBackend
import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view

from apiv2.permissions import *
from apiv2.search.fsearch import formula_indexer as fi, formula_retriever as\
    fr
from apiv2.serializers import *

logger = logging.getLogger(__name__)

schema_view = get_schema_view(title='MathQA API')

SEARCH_TYPE = "type"
VALID_QUERY_PARAMS = ["q", "query"]

SEARCH_DATABASE = "d"
SEARCH_FORMULA = "f"
SEARCH_IMAGE_TEXT = "i"
SEARCH_TAG = "t"


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


def search_database(query, request):
    questions = Question.objects.filter(content__icontains=query)
    if questions:
        serializer = (QuestionSerializer(questions,
                                         context={'request': request},
                                         many=True))
        return serializer


def search_formula(query, request):
    questions = fr.search_formula(query)
    if questions:
        serializer = QuestionSerializer(questions,
                                        context={'request': request},
                                        many=True)
        return serializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'subconcept', 'paper', 'keypoints',
                     'keywords')

    @list_route(url_path="search")
    def search(self, request):
        params = request.query_params

        for p in VALID_QUERY_PARAMS:
            if p in params:
                query = params[p]

                if query:
                    # Search type specified
                    if SEARCH_TYPE in params:
                        search_type = params[SEARCH_TYPE]

                        if search_type == SEARCH_DATABASE:
                            serializer = search_database(query, request)
                        elif search_type == SEARCH_FORMULA:
                            serializer = search_formula(query, request)
                        elif search_type == SEARCH_TAG:
                            pass
                        else:
                            ParseError("Only formula, database, and text "
                                       "search are allowed")
                    # No type specified
                    else:
                        serializer = search_database(query, request)

                    if serializer:
                        return Response(serializer.data)
                    return Response(status=status.HTTP_204_NO_CONTENT)

        raise ParseError(detail="Query parameter is required.")


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
@permission_classes((permissions.AllowAny,))
def get_formula_token(request):
    pass


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


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def check_token(request):
    pass

# class QuestionSearchView(HaystackViewSet):
#     index_models = [Question]
#     serializer_class = QuestionHaystackSerializer