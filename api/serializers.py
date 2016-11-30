from rest_framework import serializers

from meas_models.models import *


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'order', 'subject')
