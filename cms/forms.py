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
    content = forms.CharField(label='Content', max_length=1000,
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Please enter ' +
                                         'Question here.',
                                         'width': "100%",
                                         'cols': "70",
                                         'rows': "10",
                                         "onkeyup": "Preview.Update()"}))
    solution = forms.CharField(label='Solution', max_length=1000,
                               widget=forms.Textarea(
                                   attrs={'placeholder': 'Please enter ' +
                                          'solution for this question here.',
                                          'width': "100%",
                                          'cols': "70",
                                          'rows': "10"}))
    answer = forms.CharField(label='Answer', max_length=1000,
                             widget=forms.Textarea(
                                   attrs={'placeholder': 'Please enter ' +
                                          'answers for this question here.',
                                          'width': "100%",
                                          'cols': "40",
                                          'rows': "10"}))
    keypoint = forms.ModelChoiceField(empty_label="Please choose KeyPoint",
                                      queryset=KeyPoint.objects.all(),
                                      required=False)
    concept = forms.ModelChoiceField(empty_label="Please choose Concept",
                                     queryset=Concept.objects.all())
    paper = forms.ModelChoiceField(empty_label="Please choose Paper",
                                   queryset=Paper.objects.all(),
                                   required=False)


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


class EditUserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    username = forms.CharField(label='User Name', max_length=200,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    email = forms.CharField(label='Email', max_length=200,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label='First Name', max_length=200,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Email', max_length=200,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last Name'}))
    is_active = forms.BooleanField(
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]))


class EditAnswerPartForm(forms.Form):
    # id = forms.CharField(widget=forms.HiddenInput())
    part_name = forms.CharField(label='Name of Part', max_length=1,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Name of Part'}),
                                required=False)
    part_content = forms.CharField(label='Content', max_length=1000,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Please enter ' +
                                              'answer here.', }),
                                   required=False)
    part_respone_type = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),)
    required = False

    subpart_name_1 = forms.CharField(label='Name of SubPart', max_length=10,
                                     widget=forms.TextInput(attrs={
                                         'placeholder': 'Name of SubPart', }),
                                     initial='i', required=False)
    subpart_content_1 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter answer.', }),
                                        required=False)
    respone_type_1 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_name_2 = forms.CharField(label='Name of SubPart', max_length=10,
                                     widget=forms.TextInput(attrs={
                                         'placeholder': 'Name of SubPart'}),
                                     initial='ii', required=False)
    subpart_content_2 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter answer.', }),
                                        required=False)
    respone_type_2 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_name_3 = forms.CharField(label='Name of SubPart', max_length=10,
                                     widget=forms.TextInput(attrs={
                                         'placeholder': 'Name of SubPart'}),
                                     initial='iii', required=False)
    subpart_content_3 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter answer.', }),
                                        required=False)
    respone_type_3 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),
        required=False)

    subpart_name_4 = forms.CharField(label='Name of SubPart', max_length=10,
                                     widget=forms.TextInput(attrs={
                                         'placeholder': 'Name of SubPart'}),
                                     initial='iv', required=False)
    subpart_content_4 = forms.CharField(label='Content', max_length=1000,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Please ' +
                                                   'enter answer.', }),
                                        required=False)
    respone_type_4 = forms.CharField(
        max_length=10., widget=forms.Select(choices=RESPONSE_TYPES),)
