from rest_framework import generics

from meas_models.models import *
from .serializers import *
from .permissions import *

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from assessment import checker as answer_checker
import json
import re


class TopicList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class ConceptList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class ConceptDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer


class PaperList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class PaperDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class QuestionList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerPartList(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = AnswerPart.objects.all()
    serializer_class = AnswerPartSerializer


class AnswerPartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = AnswerPart.objects.all()
    serializer_class = AnswerPartSerializer


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
        else:
            answerpart_id = data['id']
            subpart_no = data['subpart_no']
            answer = data['answer']
            answerpart = AnswerPart.objects.get(pk=answerpart_id)
            if subpart_no == 0:
                model_answer_content = answerpart.part_content
            elif subpart_no == 1:
                model_answer_content = answerpart.subpart_content_1
            elif subpart_no == 2:
                model_answer_content = answerpart.subpart_content_2
            elif subpart_no == 3:
                model_answer_content = answerpart.subpart_content_3
            else:
                model_answer_content = answerpart.subpart_content_4
        model_answer_list = extract_answers(model_answer_content)
        model_answer = "|".join(model_answer_list)
        correct_answer = {'answer': model_answer}
        user_answer = {'answer': answer}
        # TODO: Process wrong step
        answer_correctness, wrong_step = answer_checker.check(correct_answer, user_answer)
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
