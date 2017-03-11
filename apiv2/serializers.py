from django.contrib.auth.models import User
from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from apiv2.models import *
from apiv2.search_indexes import QuestionIndex


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('id', 'name', 'description')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'description', 'education_level')
        # depth = 1


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'subject')
        # depth = 1


class ConceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concept
        fields = ('id', 'name', 'topic')
        # depth = 1


class SubconceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subconcept
        fields = ('id', 'name', 'concept')
        # depth = 1


class KeyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPoint
        fields = ('id', 'name', 'type', 'content', 'concept')
        # depth = 1


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'name', 'content')
        # depth = 1


class PapersetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paperset
        fields = ('id', 'name', 'subject')
        # depth = 1


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('id', 'year', 'month', 'number', 'no_of_question',
                  'subject', 'paperset')
        # depth = 1


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

        fields = ('id', 'content', 'content_cleaned_text', 'concept',
                  'formula_set',
                  'is_sample', 'subconcept', 'difficulty_level', 'marks',
                  'keypoints', 'keywords',
                  'paper', 'source', 'used_for', 'response_type',
                  'question_type', 'paper')
        # depth = 1


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion

        fields = ('id', 'category', 'content', 'concept', 'is_sample',
                  'subconcept', 'difficulty_level', 'marks',
                  'paper', 'source', 'response_type',
                  'question_type', 'paper')
        # depth = 1


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'question', 'content')
        # depth = 1


class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ('id', 'content', 'categories', 'status', 'inorder_term',
                  'sorted_term', 'structure_term', 'constant_term',
                  'variable_term', 'questions', 'concept')
        # depth = 1


class FormulaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaCategory
        fields = ('name',)

        # depth = 1


class FormulaIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaIndex
        fields = ('term_index', 'docsids', 'df')

        # depth = 1


class SearchResultSerializer(serializers.Serializer):
    rel_formula = FormulaSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)


class TestFormulaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFormulaCategory
        fields = ('name',)


class TestFormulaIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFormulaIndex
        fields = ('term_index', 'docsids', 'df')


class TestFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFormula
        fields = ('id', 'content', 'categories', 'status', 'inorder_term',
                  'sorted_term', 'structure_term', 'constant_term',
                  'variable_term', 'questions')


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


class QuestionHaystackSerializer(HaystackSerializer):

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [QuestionIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = ('id', 'content', 'content_cleaned_text', 'concept', 'formula_set',
                  'is_sample', 'subconcept', 'difficulty_level', 'marks',
                  'keypoints', 'keywords',
                  'paper', 'source', 'used_for', 'response_type',
                  'question_type', 'paper')
