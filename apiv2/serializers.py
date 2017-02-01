from django.contrib.auth.models import User
from rest_framework import serializers

# from drf_haystack.serializers import HaystackSerializer
# from search.search_indexes import QuestionIndex

from apiv2.models import *


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('id', 'name', 'description')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'description', 'education_level')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'subject')


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ('id', 'name', 'topic')


class SubconceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subconcept
        fields = ('id', 'name', 'concept')


class KeyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPoint
        fields = ('id', 'name', 'type', 'content', 'concept',
                  'question_set')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'name', 'content', 'question_set')


class PapersetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('id', 'name', 'subject')


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('id', 'year', 'month', 'number', 'no_of_question',
                  'subject', 'paperset')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

        fields = ('id', 'content', 'concept', 'is_sample', 'subconcept',
                  'difficulty_level', 'marks', 'keypoints', 'keywords',
                  'paper', 'source', 'used_for', 'response_type',
                  'question_type', 'paper')


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'question', 'content')


class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ('id', 'content', 'status', 'inorder_term',
                  'sorted_term', 'structure_term', 'constant_term',
                  'variable_term', 'question', 'concept')


class FormulaIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaIndex
        fields = ('term_index', 'docsids', 'df')


class AnswerPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
        'id', 'part_name', 'part_content', 'part_respone_type',
        'subpart_name_1', 'subpart_content_1', 'respone_type_1',
        'subpart_name_2', 'subpart_content_2', 'respone_type_2',
        'subpart_name_3', 'subpart_content_3', 'respone_type_3',
        'subpart_name_4', 'subpart_content_4', 'respone_type_4',
        'question')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


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
