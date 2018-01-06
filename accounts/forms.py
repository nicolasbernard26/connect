from django.contrib.auth import authenticate, login
from django import forms
from django.shortcuts import render

from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class UserComplementForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    email = forms.EmailField(label="E-mail", max_length=30)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','background')
