# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.models import User 
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('username', 'email')
 
 
admin.site.register(Usuario,UsuarioAdmin)
