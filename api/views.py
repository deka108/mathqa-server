from meas_models.models import *

from api.serializers import UserSerializer, EducationLevelSerializer

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EducationLevelList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer


class EducationLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, )
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
