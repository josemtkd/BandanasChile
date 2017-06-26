from django import forms

class ContactoForm(forms.Form):
 	nombre = forms.CharField(label='Nombre')
    #correo = forms.CharField(label='Tu correo electronico')
    #mensaje = forms.CharField(widget=forms.Textarea)

