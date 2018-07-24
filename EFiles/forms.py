from django.contrib.auth.models import User
from django import forms

from EFiles.models import EFile


class EFileForm(forms.ModelForm):

    class Meta:
        model = EFile
        fields = ['file_name', 'file_content']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
