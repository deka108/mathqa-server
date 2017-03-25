import logging
import os

from apiv2.utils import question_util as qu, solution_util as su, \
    text_util as tu, keypoint_util as ku
from django_filters.rest_framework import DjangoFilterBackend
from drf_haystack.viewsets import HaystackViewSet
from haystack.query import SearchQuerySet
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, list_route
from rest_framework.exceptions import ParseError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.schemas import get_schema_view

from apiv2.constants import *
from apiv2.permissions import *
from apiv2.search.fsearch import formula_indexer as fi, formula_retriever as\
    fr, formula_features_extractor as ffe
from apiv2.search.test_fsearch import check_tokenizer as ct
from apiv2.serializers import *
from apiv2.unused.views_test import search_test_database, search_test_formula
from apiv2.utils import formula_util as fu

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
                     'keywords', 'formula_categories')


def search_database(query, request):
    questions = Question.objects.filter(content__icontains=query)
    results = [{"rel_formula": None, "question": question}
               for question in questions]
    print("Question found: {}".format(len(results)))

    if results:
        serializer = SearchResultSerializer(results,
                                            context={'request': request},
                                            many=True)
        return serializer


def search_text(query, request):
    query = tu.preprocess_query(query)

    questions = SearchQuerySet().filter(
        content_cleaned_text=query)[:SEARCH_LIMIT]

    results = [{"rel_formula": None, "question": question.object}
               for question in questions]
    print("Question found: {}".format(len(results)))

    if results:
        serializer = SearchResultSerializer(results,
                                            context={'request':request},
                                            many=True)
        return serializer


def search_formula(query, request):
    results = fr.search_formula(query)

    if results:
        serializer = SearchResultSerializer(results,
                                            context={'request', request},
                                            many=True)
        return serializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def search(request):
    query = request.query_params.get("query")
    search_type = request.query_params.get("type")

    if query:
        if search_type:
            if search_type == SEARCH_DATABASE:
                serializer = search_database(query, request)
            elif search_type == SEARCH_TEXT:
                serializer = search_text(query, request)
            elif search_type == SEARCH_FORMULA:
                serializer = search_formula(query, request)
            else:
                raise ParseError(FORMULA_SEARCH_NOT_ALLOWED)
        else:
            serializer = search_database(query, request)

        if serializer:
            return Response(serializer.data)
        return Response(SEARCH_NOT_FOUND, status=status.HTTP_204_NO_CONTENT)

    raise ParseError(FORMULA_SEARCH_NO_QUERY)


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
                    elif search_type == SEARCH_TEXT:
                        pass
                    raise ParseError(FORMULA_SEARCH_NOT_ALLOWED)
                else:
                    serializer = search_test_database(query, request)

                if serializer:
                    return Response(serializer.data)
                return Response(status=status.HTTP_204_NO_CONTENT)

        raise ParseError(FORMULA_SEARCH_NO_QUERY)


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
    filter_fields = ('concept', 'questions', 'categories')


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
    filter_fields = ('concept',  'type')


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = (permissions.AllowAny,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'questions')


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
                return Response(FORMULA_INDEXING_SUCCESS)
            except Exception as e:
                print(e)
                return Response(FORMULA_INDEXING_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed()


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_formula_post(request):
    if request.method == 'GET':
        return Response({"query": "\sin(x)"})
    elif request.method == 'POST':
        query = request.data.get("query")

        if query:
            results = fr.search_formula(query)
            if results:
                serializer = SearchResultSerializer(
                    results, context={'request': request}, many=True)
                return Response(serializer.data)
            else:
                return Response(SEARCH_NOT_FOUND,
                                status=status.HTTP_204_NO_CONTENT)
        raise ParseError(FORMULA_SEARCH_NO_QUERY)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def search_formula_get(request):
    if request.method == 'GET':
        query = request.query_params.get("query")

        if query:
            results = fr.search_formula(query)
            if results:
                serializer = SearchResultSerializer(
                    results, context={'request': request}, many=True)
                return Response(serializer.data)
            else:
                return Response(SEARCH_NOT_FOUND,
                                status=status.HTTP_204_NO_CONTENT)
        raise ParseError(FORMULA_SEARCH_NO_QUERY)


@api_view(['POST', 'PUT', 'PATCH'])
@permission_classes((permissions.AllowAny,))
def create_update_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        formula = request.data.get("formula")

        if formula:
            if request.method == 'POST':
                print("Formula to be inserted: " + str(formula))
                if fu.insert_formula(formula):
                    print(FORMULA_CREATION_SUCCESS)
                    return Response(FORMULA_CREATION_SUCCESS)
                print(FORMULA_CREATION_EXIST)
                return Response(FORMULA_CREATION_EXIST)

            elif request.method == 'PUT' or request.method == 'PATCH':
                print("Formula to be updated: " + str(formula))
                updated_formula = fu.update_formula(formula)
                if updated_formula:
                    serializer = FormulaSerializer(updated_formula)
                    print(FORMULA_UPDATE_SUCCESS)
                    return Response(serializer.data)
                print(FORMULA_UPDATE_FAIL)
                return Response(FORMULA_UPDATE_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(FORMULA_DB_CRUD_FAIL,
                        status=status.HTTP_400_BAD_REQUEST)

    raise AuthenticationFailed(AUTHENTICATION_FAIL)


@api_view(['PUT', 'PATCH'])
@permission_classes((permissions.IsAuthenticated,))
def update_question(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        question = request.data.get("question")
        print(question)

        if question:
            if request.method == 'PUT' or request.method == 'PATCH':
                print("Question to be updated: " + str(question))
                updated_question = qu.update_question(question)
                if updated_question:
                    serializer = QuestionSerializer(updated_question)
                    print(QUESTION_UPDATE_SUCCESS)
                    return Response(serializer.data)
                print(QUESTION_UPDATE_FAIL)
                return Response(QUESTION_UPDATE_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(QUESTION_DB_CRUD_FAIL,
                        status=status.HTTP_400_BAD_REQUEST)

    raise AuthenticationFailed(AUTHENTICATION_FAIL)


@api_view(['PUT', 'PATCH'])
@permission_classes((permissions.IsAuthenticated,))
def update_keypoint(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        keypoint = request.data.get("keypoint")
        print(keypoint)

        if keypoint:
            if request.method == 'PUT' or request.method == 'PATCH':
                print("Question to be updated: " + str(keypoint))
                updated_keypoint = ku.update_keypoint(keypoint)
                if updated_keypoint:
                    serializer = KeyPointSerializer(updated_keypoint)
                    print(QUESTION_UPDATE_SUCCESS)
                    return Response(serializer.data)
                print(QUESTION_UPDATE_FAIL)
                return Response(QUESTION_UPDATE_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(QUESTION_DB_CRUD_FAIL,
                        status=status.HTTP_400_BAD_REQUEST)

    raise AuthenticationFailed(AUTHENTICATION_FAIL)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def post_text(request):
    text = request.data.get('text')
    if text:
        print(text)
        return Response("success", status=status.HTTP_200_OK)
    print('no text')
    return Response("no text", status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def post_image(request):
    image = request.data.get('img')
    if image:
        print(image)
        fh = open("img/test.jpg", wb)
        fh.write(image)
        fh.close()
        return Response("success", status=status.HTTP_200_OK)
    print('no text')
    return Response("no text", status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
@permission_classes((permissions.IsAuthenticated,))
def update_solution(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        solution = request.data.get("solution")

        if solution:
            if request.method == 'PUT' or request.method == 'PATCH':
                print("Solution to be updated: " + str(solution))
                updated_solution = su.update_solution(solution)
                if updated_solution:
                    serializer = SolutionSerializer(updated_solution)
                    print(SOLUTION_UPDATE_SUCCESS)
                    return Response(serializer.data)
                print(SOLUTION_UPDATE_FAIL)
                return Response(SOLUTION_UPDATE_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(SOLUTION_DB_CRUD_FAIL,
                        status=status.HTTP_400_BAD_REQUEST)

    raise AuthenticationFailed(AUTHENTICATION_FAIL)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def delete_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        formula = request.data.get("formula")

        if formula:
            print("Formula to be deleted: " + str(formula))
            deleted_formula = fu.delete_formula(formula)
            if deleted_formula:
                serializer = FormulaSerializer(deleted_formula)
                print(FORMULA_DELETION_SUCCESS)
                return Response(serializer.data)
        print(FORMULA_DELETION_FAIL)
        return Response(FORMULA_DELETION_FAIL,
                        status=status.HTTP_400_BAD_REQUEST)

    raise AuthenticationFailed(AUTHENTICATION_FAIL)


class QuestionSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Question]

    serializer_class = QuestionHaystackSerializer
