from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^productos', views.lista_productos, name="productos"),
	url(r'^detalle/(?P<pk>[0-9]+)/$', views.producto_detalle, name='detalle'),
	url(r'^categorias/(?P<pk>[0-9]+)/$', views.producto_categoria, name="categorias"),
]