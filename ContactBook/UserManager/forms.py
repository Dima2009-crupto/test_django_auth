from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2",)


class LogIn(AuthenticationForm):
    username = forms.CharField(label="login"),
    passord = forms.CharField(label="passord", widget=forms.PasswordInput),
