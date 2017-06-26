# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, HttpResponse

from portal.models import Categoria, Producto, Stock

def lista_productos(request):
	data = {}
	data['object_list'] = Producto.objects.all().order_by('-creado')[:6]
	data['nueva'] = Producto.objects.filter(nueva = True).order_by('-creado')[:1]
	template_name = 'portal/producto_bandana.html'
	return render(request, template_name, data)

def bandana(request):
	return render(request, 'portal/producto_bandana.html', {})

def producto_detalle(request):
	return render(request, 'portal/producto_detalle.html', {})

def categoria_alternativa(request):
	return render(request, 'portal/prod_alternativas.html', {})

'''
def detalle_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    template_name = 'producto/producto_bandanas.html'
    return render(request, template_name, {'productos': producto})
'''