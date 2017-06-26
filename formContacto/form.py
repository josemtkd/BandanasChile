from django import forms

class ContactoForm(forms.Form):
 	mensaje= forms.CharField(label='Nombre',required=True)
    #correo = forms.CharField(label='Tu correo electronico', requred=True)
    #mensaje = forms.CharField(widget=forms.Textarea)

