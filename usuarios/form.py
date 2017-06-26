# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name','email']

class FotoForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['fotoPerfil']