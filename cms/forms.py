"""
# Name:           cms/forms.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 23 2016
# Modified by:    Phuc Le-Sanh
"""
from django import forms
# from ckeditor.widgets import CKEditorWidget

from meas_models.models import *
from meas_models.common import *


class EditTopicForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Topic name'}))
    description = forms.CharField(label='Description', max_length=1000,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'placeholder':
                                          'Topic description'}))
    order = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':
            'Order of the Topic'}))
    subject = forms.ModelChoiceField(empty_label="Please choose Subject",
                                     queryset=Subject.objects.all())


class EditConceptForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Concept name'}))
    description = forms.CharField(label='Description', max_length=1000,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                        'placeholder': 'Concept description'}))
    order = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "Please enter order."}))
    topic = forms.ModelChoiceField(empty_label="Please choose Topic",
                                   queryset=Topic.objects.all())


class EditQuestionForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    formula = forms.ModelMultipleChoiceField(queryset=Formula.objects.all(),
                                             required=False,
                                             widget=forms.SelectMultiple(
                                                 attrs={
                                                     'class': 'selectpicker',
                                                     'multiple': '',
                                                     'data-live-search':
                                                         'true',
                                                     'data-selected-text-format':
                                                         "count > 1"}))

    topic = forms.ModelChoiceField(empty_label="", required=False,
                                   queryset=Topic.objects.all(),
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'selectpicker concept',
                                           'data-live-search': 'true'}))

    concept = forms.ModelChoiceField(empty_label="",
                                     queryset=Concept.objects.all(),
                                     widget=forms.Select(
                                         attrs={
                                             'class': 'selectpicker concept',
                                             'data-live-search': 'true'}))
    question_type = forms.CharField(
        max_length=2,
        widget=forms.Select(choices=QUESTION_TYPES)
    )
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
    content = forms.CharField(label='Content', max_length=1000,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Please enter ' +
                                         'Question here.',
                                         'width': "100%",
                                         'cols': "109",
                                         'rows': "10",
                                         "onkeyup": "Preview.Update()"}))
    solution = forms.CharField(label='Solution', max_length=1000,
                               widget=forms.Textarea(
                                   attrs={'placeholder': 'Please enter ' +
                                          'solution for this question here.',
                                          'width': "100%",
                                          'cols': "109",
                                          'rows': "10",
                                          "onkeyup": "Preview2.Update()"}))
    answer = forms.CharField(label='Answer', max_length=1000, required=False,
                             widget=forms.Textarea(
                                   attrs={
                                       'placeholder': 'Please enter ' +
                                       'answers for this question here.',
                                       'width': "100%",
                                       'cols': "109",
                                       'rows': "5"}))
    keypoint = forms.ModelChoiceField(empty_label="",
                                      queryset=KeyPoint.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'selectpicker',
                                              'data-live-search': 'true'}),
                                      required=False)

    paper = forms.ModelChoiceField(empty_label="",
                                   queryset=Paper.objects.all(),
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'selectpicker',
                                           'data-live-search': 'true'}),
                                   required=False)


class SelectSubjectForm(forms.Form):
    subject = forms.ModelChoiceField(empty_label="Please choose Subject",
                                     queryset=Subject.objects.all())


class EditPaperForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    year = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "Please enter year."}))
    month = forms.CharField(
        max_length=20., widget=forms.Select(choices=MONTHS))
    number = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "Please enter number."}))
    subject = forms.ModelChoiceField(empty_label="Please choose Subject",
                                     queryset=Subject.objects.all(),
                                     required=True)


class KeyPointForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Key Point'}))
    content = forms.CharField(label='Content',
                              widget=forms.TextInput(
                                  attrs={'placeholder':
                                         'Content of Key Point'}))


class EditUserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    username = forms.CharField(label='User Name', max_length=200,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.CharField(label='Email', max_length=200,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Email'}))
    first_name = forms.CharField(label='First Name', max_length=200,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Email', max_length=200,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Last Name'}))
    is_active = forms.BooleanField(
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))


class EditAnswerPartForm(forms.Form):
    # id = forms.CharField(widget=forms.HiddenInput())
    part_name = forms.CharField(label='Name of Part', max_length=1,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Name of Part'}),
                                required=False)
    part_content = forms.CharField(label='Content', max_length=1000,
                                   widget=forms.Textarea(
                                       attrs={
                                           'cols': "59",
                                           'rows': "3",
                                           'placeholder': 'Please enter ' +
                                           'the answer of this part.', }),
                                   required=False)
    part_respone_type = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),)
    required = False

    subpart_content_1 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter the answer.',
                                                   'cols': "59",
                                                   'rows': "3", }),
                                        required=False)
    respone_type_1 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_content_2 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter the answer.',
                                                   'cols': "59",
                                                   'rows': "3", }),
                                        required=False)
    respone_type_2 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_content_3 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter the answer.',
                                                   'cols': "59",
                                                   'rows': "3", }),
                                        required=False)
    respone_type_3 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_content_4 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.Textarea(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter the answer.',
                                                   'cols': "59",
                                                   'rows': "3", }),
                                        required=False)
    respone_type_4 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),)


class EditFormulaForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Name of Formula'}))
    content = forms.CharField(label='Name', max_length=1000,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control',
                                         'placeholder': 'Content of Formula',
                                         "onkeyup": "Preview.Update()"}))


class FormulaForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Name of Formula'}))


class ContestForm(forms.Form):
    time = forms.CharField(
        widget=forms.Select(choices=CONTEST_TIME)
    )
    numer_of_questions = forms.CharField(
        widget=forms.Select(choices=NUMER_OF_QUESTIONS)
    )
    difficulty_level = forms.CharField(
        widget=forms.Select(choices=DIFFICULTIES)
    )
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())
