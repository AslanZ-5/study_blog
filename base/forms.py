from django.db import models
from django.forms import ModelForm
from .models import Room, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host','participants']


