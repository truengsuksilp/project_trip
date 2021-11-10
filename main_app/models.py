from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Extends user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=30)
    birth_date = models.DateField()