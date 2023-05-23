from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #"{% url 'index' %}"
    path('contacto/', views.contacto, name='contacto'), #"{% url 'contacto' %}"
    path('productos/', views.productos, name='productos'), #"{% url 'productos' %}"
    path('servicios/', views.servicios, name='servicios'), #"{% url 'servicios' %}"
]