import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, list_route
from rest_framework.exceptions import ParseError, AuthenticationFailed, NotFound
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view

from apiv2.permissions import *
from apiv2.search.fsearch import formula_indexer as fi, formula_retriever as fr
from apiv2.search.test_fsearch import testformula_retriever as tfr, \
    testformula_indexer as tfi
from apiv2.search.utils import formula_util as fu
from apiv2.search.test_fsearch.utils import test_formula_util as tfu
from apiv2.search.utils import formula_features_extractor as ffe
from apiv2.search.test_fsearch import check_tokenizer as ct
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


def search_test_database(query, request):
    filtered_questions = TestQuestion.objects.filter(content__icontains=query)
    if filtered_questions:
        serializer = (TestQuestionSerializer(filtered_questions,
                                             context={'request': request},
                                             many=True))
        return serializer


class TestQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('concept', 'subconcept', 'paper', 'keypoints',
                     'keywords', 'category')

    @list_route(url_path="search")
    def test_search(self, request):
        params = request.query_params

        for p in VALID_QUERY_PARAMS:
            if p in params:
                query = params[p]

                # Search type specified
                if SEARCH_TYPE in params:
                    search_type = params[SEARCH_TYPE]

                    if search_type == SEARCH_DATABASE:
                        serializer = search_test_database(query, request)
                    elif search_type == SEARCH_FORMULA:
                        serializer = search_test_formula(query, request)
                    elif search_type == SEARCH_TAG:
                        pass
                    else:
                        ParseError("Only formula, database, and text "
                                   "search are allowed")
                else:
                    serializer = search_test_database(query, request)

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
    filter_fields = ('concept', 'questions')


class FormulaCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FormulaCategory.objects.all()
    serializer_class = FormulaCategorySerializer
    permission_classes = (permissions.AllowAny, )


class FormulaIndexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FormulaIndex.objects.all()
    serializer_class = FormulaIndexSerializer
    permission_classes = (permissions.AllowAny,)


class TestFormulaCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestFormulaCategory.objects.all()
    serializer_class = TestFormulaCategorySerializer
    permission_classes = (permissions.AllowAny, )


class TestFormulaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestFormula.objects.all()
    serializer_class = TestFormulaSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('categories', 'questions')


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
@permission_classes((permissions.AllowAny,))
def get_questions_mathml_from_concept(request, concept_id):
    return Response(ct.check_question_token_from_concept(concept_id))


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def check_token(request, concept_id):
    return Response(ct.check_question_token_from_concept(concept_id))


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_token_questions(request):
    questions = request.data.get("data").split(' ')
    return Response(questions)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_mathml_str(request):
    formula_str = request.data.get("formula")
    return Response(ffe._generate_mathmlstr(formula_str))

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_formula_token(request):
    formula_str = request.data.get("formula")
    return Response(ffe.generate_features(formula_str))


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def reindex_all_formula(request):
    if request.method == 'GET':
        return Response(
            {"username": "admin", "password": "123456", "reset": True})
    elif request.method == 'POST':
        user = request.data.get("username")
        pw = request.data.get("password")
        if user == "admin" and pw == "123456":
            try:
                fi.reindex_all_formulas()
                return Response("Formula and formula index table has been " +
                            "reindexed successfully.")
            except Exception as e:
                print(e)
                return NotFound("Unable to reindex the formula and formula "
                                "index table.")
        return AuthenticationFailed("You must be an admin to perform database "
                            "manipulation.")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_formula(request):
    if request.method == 'GET':
        return Response({"query": "\sin(x)"})
    elif request.method == 'POST':
        query = request.data.get("query")
        if query:
            results = fr.search_formula(query)
            if results:
                serializer = FormulaSearchResultSerializer(
                    results, context={'request': request}, many=True)
                return Response(serializer.data)
        else:
            ParseError("Unable to search: query unavailable")


@api_view(['POST', 'PUT', 'PATCH'])
@permission_classes((permissions.AllowAny,))
def create_update_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        formula = request.data.get("formula")

        if formula:
            if request.method == 'POST':
                if fu.insert_formula(formula):
                    return Response("Test formula has been created "
                                    "successfully.")
                return Response("Test formula already exist in the database. "
                                "But I added new question id to that formula "
                                "if it doesn't exist before")

            elif request.method == 'PUT' or request.method == 'PATCH':
                if fu.update_formula(formula):
                    return Response("Test formula has been updated "
                                    "successfully.")
                return Response("Fails to update test formula.")
        return Response("Fails to manipulate test formula database")

    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def delete_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        formula = request.data.get("formula")

        if formula:
            if fu.delete_formula(formula):
                return Response("Test formula has been deleted "
                                "successfully.")
            return Response("Fails to delete test formula.")
        return Response("Fails to manipulate test formula database")

    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def reindex_test_formula(request):
    if request.method == 'GET':
        return Response(
            {"username": "admin", "password": "123456", "reset": True})
    elif request.method == 'POST':
        user = request.data.get("username")
        pw = request.data.get("password")
        if user == "admin" and pw == "123456":
            try:
                tfi.reindex_test_formulas()
                return Response("Formula and formula index table has been " +
                            "reindexed successfully.")
            except Exception as e:
                print(e)
                return NotFound("Unable to reindex the formula and formula "
                                "index table.")
        return AuthenticationFailed("You must be an admin to perform database "
                            "manipulation.")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_test_formula(request):
    if request.method == 'GET':
        return Response({"query": "\sin(x)"})
    elif request.method == 'POST':
        query = request.data.get("query")
        if query:
            rel_formulas = tfr.search_formula(query)
            if rel_formulas:
                serializer = TestFormulaSerializer(rel_formulas,
                                                   context={'request': request},
                                                   many=True)
                return Response(serializer.data)
            return Response("Unable to find related formulas")
        else:
            ParseError("Unable to search: query unavailable")


@api_view(['POST', 'PUT', 'PATCH'])
@permission_classes((permissions.AllowAny,))
def create_update_test_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        test_formula = request.data.get("formula")

        if test_formula:
            if request.method == 'POST':
                if tfu.insert_test_formula(test_formula):
                    return Response("Test formula has been created "
                                    "successfully.")
                return Response("Test formula already exist in "
                                    "the database.")

            elif request.method == 'PUT' or request.method == 'PATCH':
                if tfu.update_test_formula(test_formula):
                    return Response("Test formula has been updated "
                                    "successfully.")
                return Response("Fails to update test formula.")
        return Response("Fails to manipulate test formula database")

    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def delete_test_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        test_formula = request.data.get("formula")

        if test_formula:
            if tfu.delete_test_formula(test_formula):
                return Response("Test formula has been deleted "
                                "successfully.")
            return Response("Fails to delete test formula.")
        return Response("Fails to manipulate test formula database")

    else:
        return Response("You must be an admin to perform database "
                        "manipulation.")