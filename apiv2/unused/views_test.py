from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed, ParseError, \
    NotFound
from rest_framework.response import Response

from apiv2.models import TestQuestion
from apiv2.search.constants import *
from apiv2.search.test_fsearch import testformula_indexer as tfi
from apiv2.search.test_fsearch.utils import test_formula_util as tfu
from apiv2.serializers import TestQuestionSerializer, TestFormulaSerializer


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
                return Response(FORMULA_TEST_INDEXING_SUCCESS)
            except Exception as e:
                print(e)
                return Response(FORMULA_TEST_INDEXING_FAIL,
                                status=status.HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed(AUTHENTICATION_FAIL)


def search_test_database(query, request):
    filtered_questions = TestQuestion.objects.filter(content__icontains=query)
    if filtered_questions:
        serializer = (TestQuestionSerializer(filtered_questions,
                                             context={'request': request},
                                             many=True))
        return serializer


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
            return Response(FORMULA_SEARCH_NOT_FOUND,
                            status=status.HTTP_204_NO_CONTENT)
        raise ParseError(FORMULA_SEARCH_NO_QUERY)


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
                    return Response(FORMULA_TEST_CREATION_SUCCESS)
                return Response(FORMULA_TEST_CREATION_EXIST)

            elif request.method == 'PUT' or request.method == 'PATCH':
                if tfu.update_test_formula(test_formula):
                    return Response(FORMULA_TEST_UPDATE_SUCCESS)
                return Response(FORMULA_TEST_UPDATE_FAIL)
        return Response(FORMULA_TEST_DB_CRUD_FAIL)

    raise AuthenticationFailed(Response(AUTHENTICATION_FAIL))


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def delete_test_formula(request):
    user = request.data.get("username")
    pw = request.data.get("password")
    if user == "admin" and pw == "123456":
        test_formula = request.data.get("formula")

        if test_formula:
            if tfu.delete_test_formula(test_formula):
                return Response(FORMULA_TEST_DELETION_SUCCESS)
            raise NotFound(FORMULA_TEST_DELETION_FAIL)
        return Response(FORMULA_TEST_DB_CRUD_FAIL)

    raise AuthenticationFailed(Response(AUTHENTICATION_FAIL))