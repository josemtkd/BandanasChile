from django.conf.urls import include, url
from django.contrib import admin

from views import Login
from . import views


urlpatterns = [
	url(r'^login', Login.as_view(), name="login"),
	url(r'^logout', views.logout, name="logout"),
	url(r'^registro', views.registro, name="registro"),
]