from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, default=None)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(null=True, default=None)
    profile_picture = models.ImageField(null=True, blank=True, upload_to=".")


def __str__(self):
        return f"{self.first_name} {self.last_name}"
