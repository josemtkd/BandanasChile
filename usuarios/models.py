# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	telefono = models.IntegerField(default=0)
	fotoPerfil = models.ImageField(upload_to='fotoPerfil',verbose_name='Imagen de Perfil', null = True)


class Direccion(models.Model):
	calle = models.CharField(verbose_name='Calle', max_length=144)
	numero = models.IntegerField()
	block = models.IntegerField()
	dep = models.IntegerField()
	region = models.CharField(verbose_name='Region', max_length=144)
	ciudad = models.CharField(verbose_name='Ciudad', max_length=144)
	comuna = models.CharField(verbose_name='Comuna', max_length=144)

