from django.contrib.auth.models import User
from rest_framework import serializers

# from drf_haystack.serializers import HaystackSerializer
# from search.search_indexes import QuestionIndex

from apiv2.models import *


class EducationLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('url', 'id', 'name', 'description')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'id', 'name', 'description', 'education_level')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'id', 'name', 'subject')


class ConceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concept
        fields = ('url', 'id', 'name', 'topic')


class SubconceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subconcept
        fields = ('url', 'id', 'name', 'concept')


class KeyPointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyPoint
        fields = ('url', 'id', 'name', 'type', 'content', 'concept',
                  'question_set')


class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keyword
        fields = ('url', 'id', 'name', 'content', 'question_set')


class PapersetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('url', 'id', 'name', 'subject')


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('url', 'id', 'year', 'month', 'number', 'no_of_question',
                  'subject', 'paperset')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question

        fields = ('url', 'id', 'content', 'concept', 'is_sample', 'subconcept',
                  'difficulty_level', 'marks', 'keypoints', 'keywords',
                  'paper', 'source', 'used_for', 'response_type',
                  'question_type', 'paper')


class SolutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solution
        fields = ('url', 'id', 'question', 'content')


class FormulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formula
        fields = ('url', 'id', 'content', 'status', 'inorder_term',
                  'sorted_term', 'structure_term', 'constant_term',
                  'variable_term', 'question', 'concept')


class FormulaIndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormulaIndex
        fields = ('term_index', 'docsids', 'df')


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email')


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
