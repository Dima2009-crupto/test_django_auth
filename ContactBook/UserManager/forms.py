from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    class Meta:
        model = User
        field = ("username","first_name","last_name", "password1", "passord2",)


class LogIn(AuthenticationForm):
    username = forms.CharField(label="login"),
    passord = forms.CharField(label="passord", widget=forms.PasswordInput)
