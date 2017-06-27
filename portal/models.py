# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField


class Categoria(models.Model):
	nombre = models.CharField(max_length=144)
	creado = models.DateTimeField(auto_now_add=True)
	precio = models.DecimalField(max_digits=10, decimal_places=0,default=2000)

	def __str__(self):
		return (self.nombre)

class Producto(models.Model):
	nombre = models.CharField(verbose_name='Nombre', max_length=144)
	descripcion = models.TextField(verbose_name='Descripción')
	nueva = models.BooleanField(verbose_name='Nueva')
	categoria = models.ForeignKey(Categoria,verbose_name='Categoría')
	#stock = models.ForeignKey(Stock,verbose_name='Stock')
	creado= models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to='imagenes',verbose_name='photo')

	def __str__(self):
		return (self.nombre)


class Stock(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
	modificada = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.cantidad)

'''
class Carrito(models.Model):
	user = models.ForeignKey(Usuario)
    active = models.BooleanField(verbose_name='Activa')
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return (self.user)
'''

class AgregarProducto(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
	fecha_pedido = models.DateField(null=True)

	def __str__(self):
		return (self.producto)