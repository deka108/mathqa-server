from django import forms


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
