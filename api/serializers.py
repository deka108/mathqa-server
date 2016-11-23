"""
# Name:           api/serializers.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""
from meas_models.models import *

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    education_levels = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EducationLevel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'education_levels')


class EducationLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationLevel
        fields = ('id', 'name', 'description')


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'order', 'subject')
