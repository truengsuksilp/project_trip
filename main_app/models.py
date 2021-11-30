from django.db.models import Model, OneToOneField, CASCADE, CharField, ForeignKey, TextField, DateTimeField, SlugField, DateField

from django.contrib.auth.models import User

# Create your models here.

# Extends user model
class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    bio = TextField(max_length=500)
    location = CharField(max_length=30)
    # birth_date = DateField()