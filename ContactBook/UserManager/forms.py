from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import MySuperUser
from django import forms


class SignUp(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="login", help_text="Обов'язкове. До 20 символів. Латинські букви, цифри та @/./+/-/_ лише")
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="name")
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="surname")
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="phone number", required=False)
    address = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="addres", required=False)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="password")
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="password confirmation")
         
    class Meta:
        model = MySuperUser
        fields = ("username", "first_name", "last_name", "phone_number", "address", "password1", "password2",)

class LogIn(AuthenticationForm):
    username = forms.CharField(label="login", widget=forms.TextInput(attrs={"class": "form-control"})),
    passord = forms.CharField(label="passord", widget=forms.PasswordInput(attrs={"class": "form-control"})),
