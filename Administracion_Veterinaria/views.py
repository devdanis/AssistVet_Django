from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from Administracion_Veterinaria.forms import EmpleadoForm #, ProductoForm

from Administracion_Veterinaria.models import Empleado#, Producto,Duenio

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404

# Create your views here.

def Administrador_empleados(request):
    template = loader.get_template('Administracion_Veterinaria/administrador_empleados.html')
    return HttpResponse(template.render())

"""
    IMPLEMENTACION DE CRUD DE EMPLEADO POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
"""
class Administrador_empleados_leer_empleado(ListView):
    model = Empleado
    context_object_name = 'empleado'
    template_name= 'Administracion_Veterinaria/administrador_empleados_leer_empleado.html'
    queryset= Empleado.objects.filter(baja=False)
    ordering = ['nombre']

class Administrador_empleados_crear_empleado(CreateView):
    model = Empleado
    fields = ['nombre']
    # form_class = CategoriaForm
    template_name = 'Administracion_Veterinaria/administrador_empleados_crear_empleado.html'
    success_url = reverse_lazy('administrador_empleados')

class Administrador_empleados_modificar_empleado(UpdateView):
    model = Empleado
    fields = ['nombre']
    # form_class = CategoriaForm
    template_name = 'Administracion_Veterinaria/administrador_empleados_modificar_empleado.html'
    success_url = reverse_lazy('administrador_empleados')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Empleado, pk=pk)
        return obj
    
class Administrador_empleados_eliminar_empleado(DeleteView):
    model = Empleado
    template_name = 'aAdministracion_Veterinaria/administrador_empleados_eliminar_empleado.html'
    success_url = reverse_lazy('administrador_empleados')
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(Empleado, pk=pk)
        return obj
    '''
    #se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()  # Llamada al método soft_delete() del modelo
        return HttpResponseRedirect(self.get_success_url())
    '''