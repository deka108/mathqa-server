"""
# Name:           webapp/forms.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""
from django import forms
from meas_models.models import *


class EditUserForm(forms.Form):
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


class EditUserProfileForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    username = forms.CharField(label='User Name', max_length=200,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'User Name'}),
                               required=False)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), required=False)
    email = forms.CharField(label='Email', max_length=200,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Email'}),
                            required=False)
    first_name = forms.CharField(label='First Name', max_length=200,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First Name'}),
                                 required=False)
    last_name = forms.CharField(label='Email', max_length=200,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last Name'}),
                                required=False)


class SelectSubjectForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
