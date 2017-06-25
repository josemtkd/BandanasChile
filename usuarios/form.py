# -*- coding: utf-8 -*-
from django.forms import ModelForm
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name','email','calle','numero','block','dep','region','ciudad','comuna']

