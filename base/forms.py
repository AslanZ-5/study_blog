from django.db import models
from django.forms import ModelForm
from .models import Room, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host','participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']