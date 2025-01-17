from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'ISBN', 'price', 'stock_quantity']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']
