from django.urls import path
from . import views

urlpatterns = [
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'), #"{% url 'confirmar_compra' %}"
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'), #"{% url 'iniciar_sesion' %}"

    ###########         CRUD de Carrito de Compras hechas por el usuario         ########
    path('crear_carrito_de_compra/', views.crear_carrito_de_compra, name='crear_carrito_de_compra'), #"{% url 'crear_carrito_de_compra' %}"
    path('leer_carrito_de_compra/', views.leer_carrito_de_compra, name='leer_carrito_de_compra'), #"{% url 'leer_compra' %}"
    path('modificar_carrito_de_compra/', views.modificar_carrito_de_compra, name='modificar_carrito_de_compra'), #"{% url 'modificar_compra' %}"
    path('borrar_carrito_de_compra/', views.borrar_carrito_de_compra, name='borrar_carrito_de_compra'), #"{% url 'borrar_compra' %}"

    ###########         CRUD de altas/bajas de usuario         ########
    path('crear_usuario/', views.registro, name='registro'), #"{% url 'registro' %}"
    path('leer_usuario/', views.leer_usuario, name='leer_usuario'), #"{% url 'leer_usuario' %}"
    path('modificar_usuario/', views.modificar_usuario, name='modificar_usuario'), #"{% url 'modificar_datos' %}"
    path('borrar_usuario/', views.borrar_usuario, name='borrar_usuario'), #"{% url 'borrar_usuario' %}"
]