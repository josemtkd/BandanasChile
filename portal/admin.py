# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Categoria,Producto, Stock

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'categoria', 'creado', 'photo')
	list_filter = ('categoria'),
	list_search = ('nombre','destacada')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'creado', 'precio')
	
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)

