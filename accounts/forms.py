from django.contrib.auth import authenticate, login
from django import forms

from django.shortcuts import render

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)