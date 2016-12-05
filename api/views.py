from rest_framework import generics

from meas_models.models import *
from .serializers import *
from .permissions import *


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
