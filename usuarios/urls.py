from django.conf.urls import include, url
from django.contrib import admin

from views import Login, Registro
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^login', Login.as_view(), name="login"),
	url(r'^logout', views.logout, name="logout"),
	url(r'^registro', Registro.as_view(), name="registro"),
	url(r'^perfil', views.perfil, name="perfil"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)