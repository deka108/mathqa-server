"""
Reconstruct the model from previous project to preserve the question data set.
"""
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from rest_framework.exceptions import ValidationError

from meas_models.common import *


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

    name = models.CharField(max_length=200, unique=True, blank=False)
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


# Block
class Topic(models.Model):
    """
    List of topics in each subject. Examples:
        Quadratic Equations & inequalities
        Indices, Surds, Exponential, Logarithms
        ...
    """

    def __str__(self):
        return self.name

    topic_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


# Topic Id
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
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


# Hidden,  used for display only
class Subtopic(models.Model):
    concept = models.ForeignKey(Concept, null=True)
    title = models.TextField(null=True)

    def __str__(self):
        return str(self.name)


# TagDefinitions which have the type of K or F
class KeyPoint(models.Model):
    """
    List of key points associate with specific concept
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    keypoint_type = models.CharField(max_length=200)
    content = models.TextField()
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)


class Keywords(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()


class Question(models.Model):
    """
    List of questions
    """

    def __str__(self):
        return self.content

    id = models.CharField(max_length=64, primary_key=True, null=False)
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPES,
        default="EX",
        blank=True)
    used_for = models.CharField(
        max_length=2,
        choices=USED_FOR,
        default="ON",
        blank=True)
    marks = models.IntegerField(default=1)
    difficulty_level = models.CharField(
        max_length=1,
        choices=DIFFICULTIES,
        default="1")
    response_type = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT)
    source = models.TextField('source', null=False)
    content = models.TextField(null=False, blank=False)
    solution = models.ForeignKey(Solution, blank=True)

    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, null=True, on_delete=models.CASCADE)
    keypoint = models.ForeignKey(KeyPoint, on_delete=models.CASCADE,
                                 null=True, blank=True)
    paper = models.ForeignKey(
        Paper, on_delete=models.CASCADE, null=True, blank=True)

    def get_difficulty_level(self):
        return range(0, int(self.difficulty_level))


class Solution(models.Model):
    """
    List of Solutions
    """
    question = models.ForeignKey(Question, null=False)
    content = models.TextField()

    def __str__(self):
        return str(self.id)


class Formula(models.Model):
    """
    List of formula
    """

    def __str__(self):
        return self.content

    content = models.TextField()
    status = models.BooleanField(default=False)
    inorder_term = models.CharField(max_length=1024, null=True, blank=True)
    sorted_term = models.CharField(max_length=1024, null=True, blank=True)
    structure_term = models.CharField(max_length=1024, null=True, blank=True)
    constant_term = models.CharField(max_length=1024, null=True, blank=True)
    variable_term = models.CharField(max_length=1024, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 null=True, blank=True)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE,
                                null=True, blank=True)


class FormulaIndex(models.Model):
    """
    List of Formula Indices
    """
    term_index = models.CharField('index key', primary_key=True,
                                  max_length=255)
    docsids = models.TextField(null=True, blank=True)
    df = models.PositiveIntegerField('frequency', default=1, blank=True)


class Paperset(models.Model):
    """
    Category of papers.
    """
    title = models.TextField('title', null=True)
    subject = models.ForeignKey(Subject, null=False)

    def __str__(self):
        return str(self.title)


class Paper(models.Model):
    """
    List of paper
    """

    def __str__(self):
        return str(self.year) + " " + str(self.get_month_display()) + " " + \
               str(self.number)

    year = models.IntegerField()
    month = models.CharField(max_length=20, choices=MONTHS, default="1")
    number = models.IntegerField()
    no_of_question = models.IntegerField(null=True, blank=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                default=1)


class Image(models.Model):
    """
    List of Images
    """
    qa = models.TextField(null=True)
    qa_id = models.ForeignKey(Question, null=False)
    imagepath = models.FileField(upload_to="/static/image/")

    def __str__(self):
        return str(self.id)


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
