from rest_framework import serializers

from meas_models.models import *


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'order', 'subject')


class ConceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concept
        fields = ('id', 'name', 'description', 'topic')


class PaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paper
        fields = ('id', 'year', 'month', 'number', 'no_of_question')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question_type', 'source', 'used_for', 'mark',
                  'difficulty_level', 'respone_type', 'content', 'solution',
                  'concept', 'keypoint', 'paper')


class AnswerPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'part_name', 'part_content', 'part_respone_type',
                  'subpart_name_1', 'subpart_content_1', 'respone_type_1',
                  'subpart_name_2', 'subpart_content_2', 'respone_type_2',
                  'subpart_name_3', 'subpart_content_3', 'respone_type_3',
                  'subpart_name_4', 'subpart_content_4', 'respone_type_4',
                  'question')
