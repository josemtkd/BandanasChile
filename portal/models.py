# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=144)
	creada = models.DateTimeField(auto_now_add=True)
	precio = models.DecimalField(max_digits=10, decimal_places=0,default=2000)

	def __str__(self):
		return (self.nombre)

class Bandana(models.Model):
	nombre = models.CharField(verbose_name='Nombre', max_length=144)
	description = models.TextField(verbose_name='Descripción')
	nueva = models.BooleanField(verbose_name='Nueva')
	categoria = models.ForeignKey(Categoria,verbose_name='Categoría')
	agregada= models.DateTimeField(auto_now_add=True)
	modificada = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to='notice_image',blank=True,verbose_name='photo')
		


	def __str__(self):
		return (self.nombre)