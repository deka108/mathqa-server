from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import User

NUMERIC = 'Numberic'
SKETCH = 'Sketch'
EXPRESSION = 'EXPRESSION'
TEXT = 'Text'
PROVE = 'Prove'

RESPONSE_TYPES = [
    (NUMERIC, 'Exam Numberic'),
    (SKETCH, 'Sketch'),
    (EXPRESSION, 'Expression'),
    (TEXT, 'Text'),
    (PROVE, 'Prove')
]
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

    name = models.CharField(max_length=200)
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

    name = models.CharField(max_length=200)
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

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    order = models.PositiveIntegerField(null=True, blank=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Concept(models.Model):
    """
    List of concepts in each topic. Examples:
        Quadratic Equations & inequalities has:
            Symmetric properties of the roots of a quadratic equation
        ...
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Test(models.Model):
    """
    List of test
    """

    ADAPTIVE_TEST = "AP"
    CONTEST = "CT"

    TEST_TYPES = [
        (ADAPTIVE_TEST, 'Adaptive Test'),
        (CONTEST, 'Contest')
    ]

    name = models.CharField(max_length=200)
    test_type = models.CharField(
        max_length=200,
        choices=TEST_TYPES,
        default=ADAPTIVE_TEST)


class Question(models.Model):
    """
    List of questions
    """

    EXAM_PAPERS = "EP"
    ONLINE = "OL"

    QUESTION_SOURCES = [
        (EXAM_PAPERS, 'Exam papers'),
        (ONLINE, 'Online')
    ]

    content = models.TextField(max_length=1000)
    source = models.CharField(
        max_length=2,
        choices=QUESTION_SOURCES,
        default=EXAM_PAPERS)
    difficulty_level = models.IntegerField(
        validators=[validate_difficulty_range],
        default=0)

    parent = models.ForeignKey("self", null=True)
    tests = models.ManyToManyField(Test)


class Proficiency(models.Model):
    """
    Track history of students
    """

    detail = models.IntegerField
    response = models.TextField(max_length=1000)
    respone_type = models.CharField(
        max_length=10,
        choices=RESPONSE_TYPES,
        default=TEXT)
    is_complete = models.BooleanField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    unique_together = ("user", "restaurant", "detail")
