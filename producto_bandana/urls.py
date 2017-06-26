from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^producto_bandana', views.lista_productos, name="producto_bandana"),
	url(r'^detalle', views.producto_detalle, name="detalle"),
	url(r'^categoria_alternativa', views.categoria_alternativa, name="alternativas"),
]