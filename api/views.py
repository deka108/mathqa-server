# from drf_haystack.viewsets import HaystackViewSet
import json
import logging
import re

from assessment import checker as answer_checker
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from search.fsearch import formula_clustering as fc
from search.fsearch import formula_indexer as fi
from search.fsearch import formula_transformer as ft
from search.fsearch import formula_retriever as fr
from .permissions import *
from .serializers import *

logger = logging.getLogger(__name__)


class TopicList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.all()
        subj_id = self.kwargs.get('subj_id')
        if subj_id is not None:
            queryset = queryset.filter(subject=subj_id)
        return queryset


class TopicDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ConceptList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ConceptSerializer

    def get_queryset(self):
        queryset = Concept.objects.all()
        subj_id = self.kwargs.get('subj_id')
        topic_id = self.kwargs.get('topic_id')
        if subj_id is not None:
            queryset = queryset.filter(
                topic__in=Topic.objects.filter(subject=subj_id))
        elif topic_id is not None:
            queryset = queryset.filter(topic=topic_id)

        return queryset


class ConceptDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class PaperList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class PaperDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class QuestionList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        subj_id = self.kwargs.get('subj_id')
        topic_id = self.kwargs.get('topic_id')
        concept_id = self.kwargs.get('concept_id')

        if "sample" in self.request.path:
            queryset = queryset.filter(keypoint__isnull=False)
        elif "real" in self.request.path:
            queryset = queryset.filter(keypoint__isnull=True)

        if subj_id is not None:
            queryset = queryset.filter(concept__in=Concept.objects.filter(
                topic__in=Topic.objects.filter(subject=subj_id)))
        elif topic_id is not None:
            queryset = queryset.filter(
                concept__in=Concept.objects.filter(topic=topic_id))
        elif concept_id is not None:
            queryset = queryset.filter(concept=concept_id)

        return queryset


class QuestionDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerPartList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = AnswerPart.objects.all()
    serializer_class = AnswerPartSerializer


class AnswerPartDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = AnswerPart.objects.all()
    serializer_class = AnswerPartSerializer


class SubjectList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class KeyPointList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = KeyPointSerializer

    def get_queryset(self):
        queryset = KeyPoint.objects.all()
        concept_id = self.kwargs.get('concept_id')

        if concept_id is not None:
            queryset = queryset.filter(concept=concept_id)

        return queryset


class KeyPointDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = KeyPoint.objects.all()
    serializer_class = KeyPointSerializer


class FormulaList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer


class FormulaDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer


class FormulaIndexList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = FormulaIndex.objects.all()
    serializer_class = FormulaIndexSerializer


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def reindex_all_formula(request):
    fi.reindex_all_formulas()
    return Response("Formula and formula index table has been reindexed "
                        "successfully.")


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
        query = request.data["content"]
        questions = fr.search_formula(query)
        serializer = QuestionSerializer(questions,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def search_formula_cluster(request):
    if request.method == 'GET':
        data = ft.transform_formulas()
        return Response(data)
    elif request.method == 'POST':
        query = request.data["content"]
        data = fc.generate_kmeans_cluster(query)
        return Response(data)


# class QuestionSearchView(HaystackViewSet):
#     index_models = [Question]
#     serializer_class = QuestionHaystackSerializer

# For assessment
@csrf_protect
def check_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("UTF-8"))
        if data['type'] == 'q':
            question_id = data['id']
            answer = data['answer']
            question = Question.objects.get(pk=question_id)
            model_answer_content = question.answer
            topic = question.concept.topic.name
            answer_type = question.respone_type
        else:
            answerpart_id = data['id']
            subpart_no = data['subpart_no']
            answer = data['answer']
            answerpart = AnswerPart.objects.get(pk=answerpart_id)
            topic = answerpart.question.concept.topic.name
            if subpart_no == 0:
                model_answer_content = answerpart.part_content
                answer_type = answerpart.part_respone_type
            elif subpart_no == 1:
                model_answer_content = answerpart.subpart_content_1
                answer_type = answerpart.respone_type_1
            elif subpart_no == 2:
                model_answer_content = answerpart.subpart_content_2
                answer_type = answerpart.respone_type_2
            elif subpart_no == 3:
                model_answer_content = answerpart.subpart_content_3
                answer_type = answerpart.respone_type_3
            else:
                model_answer_content = answerpart.subpart_content_4
                answer_type = answerpart.respone_type_4
        # TODO: Fix data inconsistency problem
        if answer_type == "Numberic":
            answer_type = "Numeric"
        elif answer_type == "EXPRESSION":
            answer_type = "Expression"
        model_answer_list = extract_answers(model_answer_content)
        model_answer = "|".join(model_answer_list)
        correct_answer = {'answer': model_answer}
        user_answer = {'answer': answer}
        # TODO: Process wrong step
        answer_correctness, wrong_step = answer_checker.check(correct_answer, user_answer, topic=topic, answer_type=answer_type)
        result = dict()
        if data['type'] == 'q':
            result['type'] = 'q'
            result['id'] = question_id
        else:
            result['type'] = 'a'
            result['id'] = answerpart_id
            result['subpart_no'] = subpart_no
        result['result'] = answer_correctness
    response = json.dumps(result)
    return HttpResponse(
        response,
        content_type='application/json'
    )


def extract_answers(content):
    """Extract answer fields in a string and return a list"""
    fields = re.findall(r'"(.*?)"', content)
    return fields
