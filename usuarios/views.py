# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.form import *
from django.urls import reverse


# Create your views here.
def logout(request):
  auth.logout(request)
  template_name = 'usuarios/logout.html'
  return render(request,template_name)


def perfil(request):
    template_name = 'usuarios/perfil.html'
    usuario = Usuario.objects.get(username = request.user.username)
    form = FotoForm(request.POST, request.FILES or None,instance = usuario )
    form2 = personalesForm(request.POST or None, instance = usuario )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('perfil'))
    else:
        form = FotoForm()

    if request.method == 'POST':

        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('perfil'))

        
    return render(request, template_name, {'form': form , 'form2': form2 })

class Login(FormView):
    
    template_name = 'usuarios/login.html'
    
    form_class = AuthenticationForm
    
    success_url =  reverse_lazy("perfil")
 
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
 
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


class Registro(CreateView):
	model = Usuario
	template_name = 'usuarios/registro.html'
	form_class = UsuarioForm
	success_url = reverse_lazy('login')



















