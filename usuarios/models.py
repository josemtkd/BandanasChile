# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
	telefono = models.IntegerField(default=0)
	fotoPerfil = models.ImageField(upload_to='fotoPerfil',verbose_name='Imagen de Perfil', null = True)


