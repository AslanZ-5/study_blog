from telnetlib import STATUS
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from base.models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
    # def clean_email(self):
    #     email= self.cleaned_data.get('email')
    #
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email is taken')

        


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']