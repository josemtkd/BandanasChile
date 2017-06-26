from django.conf.urls import url
from . import views
from formContacto.views import contacto

urlpatterns = [
url(r'^contacto/$', views.contacto, name="contacto"),
]