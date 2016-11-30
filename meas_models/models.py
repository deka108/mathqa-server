"""
# Name:           meas_models/models.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 16 2016
# Last Modified:  Nov 23 2016
# Modified by:    Phuc Le-Sanh
"""
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from common import *

"""
Validations
"""


def validate_difficulty_range(value):
    if value < 1 or value > 10:
        raise ValidationError(
            _('%(value)s is out of correct range of difficulty level.'),
            params={'value': value},
        )


class EducationLevel(models.Model):
    """
    List of education levels. Examples:
        A'level
        O'level
        Elementary
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)


class Subject(models.Model):
    """
    List of subjects in specific education level. Examples:
        Additional Mathematics
        Elementary Mathematics
        H2 Mathematics
        PSLE Mathematics
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)

    education_level = models.ForeignKey(
        EducationLevel, on_delete=models.CASCADE)


class Topic(models.Model):
    """
    List of topics in each subject. Examples:
        Quadratic Equations & inequalities
        Indices, Surds, Exponential, Logarithms
        ...
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)
    order = models.PositiveIntegerField(null=True, blank=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def as_json(self):
        return dict(
            topic_id=self.id,
            name=self.name,
            description=self.description,
            order=self.order,
            subject=self.subject.name)


class Concept(models.Model):
    """
    List of concepts in each topic. Examples:
        Quadratic Equations & inequalities has:
            Symmetric properties of the roots of a quadratic equation
        ...
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Test(models.Model):
    """
    List of test
    """

    name = models.CharField(max_length=200)
    test_type = models.CharField(
        max_length=200,
        choices=TEST_TYPES,
        default=PRACTICE_TEST)
    questions_list = models.TextField()
    number_of_questions = models.IntegerField()


class Paper(models.Model):
    """
    List of paper
    """

    def __str__(self):
        return str(self.year) + " " + str(self.get_month_display()) + " " +\
            str(self.number)

    year = models.IntegerField()
    month = models.CharField(max_length=20, choices=MONTHS, default="1")
    number = models.IntegerField()
    no_of_question = models.IntegerField(null=True, blank=True)


class KeyPoint(models.Model):
    """
    List of key points associate with specific concept
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    content = models.TextField()

    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)


class Question(models.Model):
    """
    List of questions
    """

    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPES,
        default="EX")
    source = models.CharField(
        max_length=2,
        choices=QUESTION_SOURCES,
        default="EP")
    used_for = models.CharField(
        max_length=2,
        choices=USED_FOR,
        default="ON")
    mark = models.IntegerField(default=1)
    difficulty_level = models.CharField(
        max_length=1,
        choices=DIFFICULTIES,
        default="1")
    respone_type = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT)
    content = RichTextField()
    solution = RichTextField()
    answer = RichTextField(default="Test")

    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    keypoint = models.ForeignKey(KeyPoint, on_delete=models.CASCADE,
                                 null=True, blank=True)
    paper = models.ForeignKey(
        Paper, on_delete=models.CASCADE, null=True, blank=True)

    def get_difficulty_level(self):
        return range(0, int(self.difficulty_level))


class AnswerPart(models.Model):
    """
    List of AnswerPart
    """

    part_name = models.CharField(max_length=1)
    part_content = RichTextField()
    part_respone_type = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT)
    subpart_name_1 = models.CharField(max_length=10, null=True, blank=True)
    subpart_content_1 = RichTextField(null=True, blank=True)
    respone_type_1 = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT, null=True, blank=True)
    subpart_name_2 = models.CharField(max_length=10, null=True, blank=True)
    subpart_content_2 = RichTextField(null=True, blank=True)
    respone_type_2 = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT, null=True, blank=True)
    subpart_name_3 = models.CharField(max_length=10, null=True, blank=True)
    subpart_content_3 = RichTextField(null=True, blank=True)
    respone_type_3 = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT, null=True, blank=True)
    subpart_name_4 = models.CharField(max_length=10, null=True, blank=True)
    subpart_content_4 = RichTextField(null=True, blank=True)
    respone_type_4 = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT, null=True, blank=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
