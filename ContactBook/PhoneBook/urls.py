from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_contacts, name= "get_contacts"),
    path("contacts/add", views.add_contact, name="add_contact"),
   # path("delete_contact/<int:id>", views.delete_contact, name="delete_contact"),
    #path("edit_contact/<int:id>", views.edit_contact, name="edit_contact")
]