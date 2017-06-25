# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Usuario

# Register your models here.
class UsuariorAdmin(admin.ModelAdmin):
	list_display = ('username', 'email')