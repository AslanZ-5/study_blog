from django.db import models
from django.forms import ModelForm
from .models import Room, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class RoomForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Room
        exclude = ['host','participants','captcha']


