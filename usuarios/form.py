# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

