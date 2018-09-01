from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Books.models import Book , RequestedBooks


class BookForm(forms.ModelForm):

    taken_by = forms.CharField(required=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'book_logo', 'description']

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        User._meta.get_field("email")._unique = True

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)



    class Meta:
        model = User
        fields = ['username', 'email', 'password']




class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RequestedBooksForm(forms.ModelForm):
    title=forms.CharField(required=True)
    author=forms.CharField(required=False)
    RequestedBooks._meta.get_field("title")._unique = True
    #publisher=forms.CharField(required=False)
    class Meta:
        model=RequestedBooks
        fields=['title' , 'author' ]



