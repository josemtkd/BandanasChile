# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, HttpResponse, get_object_or_404

from portal.models import Categoria, Producto, Stock#, Carrito

def lista_productos_carrito(request):
	data = {}
	data['object_list'] = Producto.objects.all().order_by('-creado')[:6]
	data['nueva'] = Producto.objects.filter(nueva = True).order_by('-creado')[:9]
	data['categoria'] = Categoria.objects.all()
	template_name = 'carrito_compras/productos_en_carrito.html'
	return render(request, template_name, data)

def agregar_producto(request, pk):
	producto = get_object_or_404(Producto, pk=pk)
	carrito,created = Cart.objects.get_or_create(user=request.usuario, activate=True)
	carrito.agregar_producto(pk)
	
	return redirect('carrito')

'''
def agregar_al_carro(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    carrito,created = Carrito.objects.get_or_create(user=request.user, active=True)
    order,created = AgregarProducto.objects.get_or_create(book=book,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    return redirect('cart')
  '''