from django.contrib.auth.models import User
# from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
# from search.search_indexes import QuestionIndex
from meas_models.models import *


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'id', 'name', 'description', 'order', 'subject')


class ConceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concept
        fields = ('url', 'id', 'name', 'description', 'topic')


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('url', 'id', 'year', 'month', 'number', 'no_of_question')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question

        fields = ('url', 'id', 'question_type', 'used_for', 'mark',
                  'difficulty_level', 'respone_type', 'content', 'solution',
                  'concept', 'keypoint', 'paper')


class AnswerPartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
        'url', 'id', 'part_name', 'part_content', 'part_respone_type',
        'subpart_name_1', 'subpart_content_1', 'respone_type_1',
        'subpart_name_2', 'subpart_content_2', 'respone_type_2',
        'subpart_name_3', 'subpart_content_3', 'respone_type_3',
        'subpart_name_4', 'subpart_content_4', 'respone_type_4',
        'question')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'id', 'name', 'description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email')


class KeyPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyPoint
        fields = ('url', 'id', 'name', 'content', 'concept')


class FormulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formula
        fields = ('url', 'id', 'content', 'status', 'inorder_term',
                  'sorted_term', 'structure_term', 'constant_term',
                  'variable_term')


class FormulaIndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormulaIndex
        fields = ('indexkey', 'docsids', 'df')

# class QuestionHaystackSerializer(HaystackSerializer):

#     class Meta:
#         # The `index_classes` attribute is a list of which search indexes
#         # we want to include in the search.
#         index_classes = [QuestionIndex]

#         # The `fields` contains all the fields we want to include.
#         # NOTE: Make sure you don't confuse these with model attributes. These
#         # fields belong to the search index!
#         fields = ["text", "question_type", "used_for", "mark", 
#                   "difficulty_level", "respone_type", "content",
#                   "solution", "answer", "concept", "keypoint"]
