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
    order = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Please enter order."}))
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
    mark = forms.IntegerField(
        widget=forms.Select(choices=MARKS))
    difficulty_level = forms.CharField(
        max_length=1, widget=forms.Select(choices=DIFFICULTIES))
    respone_type = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES))
    content = forms.CharField(widget=CKEditorWidget())
    solution = forms.CharField(widget=CKEditorWidget())
    concept = forms.ModelChoiceField(empty_label="Please choose Concept",
                                     queryset=Concept.objects.all())
    paper = forms.ModelChoiceField(empty_label="Please choose Paper",
                                   queryset=Paper.objects.all(),
                                   required=False)

    # Part 1
    id_1 = forms.CharField(widget=forms.HiddenInput())
    mark_1 = forms.IntegerField(
        widget=forms.Select(choices=MARKS), required=False)
    difficulty_level_1 = forms.CharField(max_length=1,
                                         widget=forms.Select(
                                             choices=DIFFICULTIES),
                                         required=False)
    respone_type_1 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)
    content_1 = forms.CharField(widget=CKEditorWidget(), required=False)
    solution_1 = forms.CharField(widget=CKEditorWidget(), required=False)

    # Part 2
    id_1 = forms.CharField(widget=forms.HiddenInput())
    mark_2 = forms.IntegerField(
        widget=forms.Select(choices=MARKS), required=False)
    difficulty_level_2 = forms.CharField(max_length=1,
                                         widget=forms.Select(
                                             choices=DIFFICULTIES),
                                         required=False)
    respone_type_2 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)
    content_2 = forms.CharField(widget=CKEditorWidget(), required=False)
    solution_2 = forms.CharField(widget=CKEditorWidget(), required=False)

    # Part 3
    id_1 = forms.CharField(widget=forms.HiddenInput())
    mark_3 = forms.IntegerField(
        widget=forms.Select(choices=MARKS), required=False)
    difficulty_level_3 = forms.CharField(max_length=1,
                                         widget=forms.Select(
                                             choices=DIFFICULTIES),
                                         required=False)
    respone_type_3 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)
    content_3 = forms.CharField(widget=CKEditorWidget(), required=False)
    solution_3 = forms.CharField(widget=CKEditorWidget(), required=False)

    # Part 4
    id_1 = forms.CharField(widget=forms.HiddenInput())
    mark_4 = forms.IntegerField(
        widget=forms.Select(choices=MARKS), required=False)
    difficulty_level_4 = forms.CharField(max_length=1,
                                         widget=forms.Select(
                                             choices=DIFFICULTIES),
                                         required=False)
    respone_type_4 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)
    content_4 = forms.CharField(widget=CKEditorWidget(), required=False)
    solution_4 = forms.CharField(widget=CKEditorWidget(), required=False)


class SelectSubjectForm(forms.Form):
    subject = forms.ModelChoiceField(empty_label="Please choose Subject",
                                     queryset=Subject.objects.all())


class EditPaperForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    year = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Please enter year."}))
    month = forms.CharField(
        max_length=20., widget=forms.Select(choices=MONTHS))
    number = forms.IntegerField(widget=forms.TextInput(
        {"placeholder": "Please enter number."}))


class KeyPointForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Key Point'}))
    content = forms.CharField(label='Content',
                              widget=forms.TextInput(
                                  attrs={'placeholder':
                                         'Content of Key Point'}))
