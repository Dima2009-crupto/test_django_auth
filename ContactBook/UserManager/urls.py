from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("sign_up/", views.sign_up, name = "signup"),
    path("sign_in/", views.sign_in, name = "signin"),
]