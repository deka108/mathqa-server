from django import forms
from ckeditor.widgets import CKEditorWidget

from meas_models.models import *
from meas_models.common import *


class EditTopicForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Topic name'}))
    description = forms.CharField(label='Description', max_length=1000,
                                  widget=forms.Textarea(
                                      attrs={'placeholder':
                                             'Topic description'}))
    subject = forms.ModelChoiceField(empty_label="Please choose Subject",
                                     queryset=Subject.objects.all())


class EditConceptForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Concept name'}))
    description = forms.CharField(label='Description', max_length=1000,
                                  widget=forms.Textarea(
                                      attrs={'placeholder':
                                             'Concept description'}))
    topic = forms.ModelChoiceField(empty_label="Please choose Topic",
                                   queryset=Topic.objects.all())


class EditQuestionForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    question_type = forms.CharField(
        max_length=2,
        widget=forms.Select(choices=QUESTION_TYPES)
    )
    source = forms.CharField(
        max_length=2., widget=forms.Select(choices=QUESTION_SOURCES))
    used_for = forms.CharField(
        max_length=2, widget=forms.Select(choices=USED_FOR))
    number_of_part = forms.IntegerField(
        widget=forms.Select(choices=NUMBER_OF_PARTS))
    mark = forms.IntegerField()
    difficulty_level = forms.IntegerField()
    respone_type = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES))
    content = forms.CharField(widget=CKEditorWidget())
    solution = forms.CharField(widget=CKEditorWidget())
    concept = forms.ModelChoiceField(empty_label="Please choose Concept",
                                     queryset=Concept.objects.all())
    paper = forms.ModelChoiceField(empty_label="Please choose Paper",
                                   queryset=Paper.objects.all())

    class Meta:
        model = Question


class EditPartForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    mark = forms.IntegerField()
    difficulty_level = forms.IntegerField()
    respone_type = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES))
    content = forms.CharField(widget=CKEditorWidget())
    solution = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Part
