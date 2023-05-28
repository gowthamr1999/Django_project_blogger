from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default = datetime.now,blank=True)


# class ExtendedUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     First_name = models.CharField(max_length=100)
#     Last_name= models.CharField(max_length=100)
#     Gender = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     Phone_number = models.CharField(max_length=100,primary_key=True)
