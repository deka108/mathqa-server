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
