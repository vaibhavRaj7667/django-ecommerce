from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'id': 'username',
            'name': 'username'
        })
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'id': 'email',
            'name': 'email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'id': 'password1',
            'name': 'password1'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'id': 'password2',
            'name': 'password2'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
