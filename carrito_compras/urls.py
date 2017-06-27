from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^carrito', views.lista_productos_carrito, name="carrito"),
]