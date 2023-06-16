########   forms.py   ########

from django import forms
from .models import MiModelo

from django import forms
from .models import MiModelo

class MiFormulario(forms.ModelForm):
    class Meta:
        model = MiModelo
        fields = ['texto', 'numero', 'contrasena', 'usuario', 'booleano', 'opciones']
        widgets = {
            'contrasena': forms.PasswordInput(),
            'booleano': forms.CheckboxInput(),
            'opciones': forms.Select(choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2')]),
        }

########   models.py   ########
from django.db import models

class MiModelo(models.Model):
    texto = models.CharField(max_length=100)
    numero = models.IntegerField()
    contrasena = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    booleano = models.BooleanField()
    opciones = models.CharField(max_length=100, choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2')])

########   views.py   ########
from django.shortcuts import render
from .forms import MiFormulario

def mi_vista(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Realiza cualquier otra acción necesaria
            return render(request, 'exito.html')
    else:
        formulario = MiFormulario()

    return render(request, 'formulario.html', {'formulario': formulario})

########   urls.py   ########
from django.urls import path
from . import views

urlpatterns = [
    path('mi-formulario/', views.mi_vista, name='mi-formulario'),
]

