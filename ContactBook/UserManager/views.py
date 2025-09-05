from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUp, LogIn

# Create your views here.


def sign_up(request):
    print("POST?=", request.POST)

    form = SignUp(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.add_message(request=request, level=messages.SUCCESS, message="You have successfully signed up")
        return redirect("index")
    
    return render(request, "signup.html", {"form": form})


def sig_in(request):
    form = LogIn(data=request.Post or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        if user:
            login(request=request, user = user )
            messages.add_message(request=request, level=messages.SUCCESS, message="You have successfully signed in")
            return redirect("index")
        else:
            messages.add_message(request=request, level=messages.ERROR, message="Username or password is incorrect")
        
    return render(request,"signin.html", context=dict(form=form))


@login_required(login_url="/users/sig_in/")
def index(request):
    return render(request, "index.html")