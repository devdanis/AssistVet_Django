from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import core

# Create your views here.

def index(request):
    #template = loader.get_template('index.html')
    return render(request, 'tienda/index.html')

def perros(request):
    #template = loader.get_template('perros.html')
    return render(request, 'tienda/perros.html')

def gatos(request):
    #template = loader.get_template('gatos.html')
    return render(request, 'tienda/gatos.html')

def servicios(request):
    #template = loader.get_template('servicios.html')
    return render(request, 'tienda/servicios.html')

def cart(request):
    return render(request, 'tienda/cart.html')