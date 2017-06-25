# -*- coding: utf-8 -*-
from django.forms import ModelForm
from usuarios.models import Usuario, Direccion

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name','email']


class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle','numero','block','dep','region','ciudad','comuna']