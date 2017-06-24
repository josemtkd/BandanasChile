# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Categoria,Producto, Usuario

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'categoria')
	list_filter = ('categoria'),
	list_search = ('nombre','destacada')

admin.site.register(Categoria)
admin.site.register(Producto,ProductoAdmin)
