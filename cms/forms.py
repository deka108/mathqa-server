from django import forms

from meas_models.models import *


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
