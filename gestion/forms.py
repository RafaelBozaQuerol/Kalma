# gestion/forms.py

from django import forms
from .models import Cliente, Servicio, Visita, Empresa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio', 'duracion_min']

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['cliente', 'servicios', 'fecha']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion', 'telefono']     
