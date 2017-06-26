# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formContacto.form  import ContactoForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage



def contacto(request):
	template_name = 'consulta/aboutus.html'
	if request.method == 'post':
		form=ContactoForm(request.POST)
		if form.is_valid():
			titulo = 'Mensaje desde página bandanas'
			contenido = form.cleaned_data['mensaje'] +"\n"
			#contenido += 'Comunicarse a: '+ form.cleaned_data['correo']
			correo= EmailMessage (titulo,contenido, to= ['jmvc92@gmail.com'])
			correo.send()
			return	HttpResponseRedirect('asdsa')

	else:
		form =ContactoForm()

	return render(request, template_name, {'form': form})


# Create your views here.
