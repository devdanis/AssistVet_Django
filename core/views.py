from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def perros(request):
    template = loader.get_template('perros.html')
    return HttpResponse(template.render())

def gatos(request):
    template = loader.get_template('gatos.html')
    return HttpResponse(template.render())

def servicios(request):
    template = loader.get_template('servicios.html')
    return HttpResponse(template.render())