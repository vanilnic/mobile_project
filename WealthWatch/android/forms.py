from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
