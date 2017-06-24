# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=144)
	creada = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.name)

class Bandana(models.Model):
	nombre = models.CharField(verbose_name='Nombre', max_length=144)
	description = models.TextField(verbose_name='Descripción')
	nueva = models.BooleanField(verbose_name='Nueva')
	categoria = models.ForeignKey(Categoria,verbose_name='Categoría')
	agregada= models.DateTimeField(auto_now_add=True)
	modificada = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to='notice_image',blank=True)


	def __str__(self):
		return self.name