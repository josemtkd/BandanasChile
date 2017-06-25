# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Direccion(models.Model):
	calle = models.CharField(verbose_name='Calle', max_length=144)
	numero = models.IntegerField()
	block = models.IntegerField(null = True)
	dep = models.IntegerField(null = True)
	region = models.CharField(verbose_name='Region', max_length=144)
	ciudad = models.CharField(verbose_name='Ciudad', max_length=144)
	comuna = models.CharField(verbose_name='Comuna', max_length=144)


class Usuario(AbstractUser):
	direccion = models.ForeignKey(Direccion, null =True)
	telefono = models.IntegerField(null = True)

