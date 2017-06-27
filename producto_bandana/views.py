# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, HttpResponse, get_object_or_404

from portal.models import Categoria, Producto, Stock


def lista_productos(request):
	data = {}
	data['object_list'] = Producto.objects.all().order_by('-creado')[:6]
	data['nueva'] = Producto.objects.filter(nueva = True).order_by('-creado')[:9]
	data['categoria'] = Categoria.objects.all()
	template_name = 'producto_bandana/productos.html'
	return render(request, template_name, data)



def bandana(request):
	return render(request, 'producto_bandana/productos.html', {})



def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    template_name = 'producto_bandana/producto_detalle.html'
    return render(request, template_name, {'producto_detalle': producto})



def producto_categoria(request, pk):
	data = {}
	categoria = get_object_or_404(Categoria, pk=pk)
	print categoria.id
	data['productos'] = Producto.objects.filter(categoria = categoria.id)
	data['categorias'] = Categoria.objects.all()
	data['paginas'] = Categoria.objects.all()
	
	template_name = 'producto_bandana/producto_categoria.html'
	return render(request, template_name, data)