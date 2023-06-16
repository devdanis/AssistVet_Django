from django.urls import path
from . import views
#from .views import crear_carrito_de_compras


urlpatterns = [
    #Sitio general
    path('', views.index, name='index'), #"{% url 'index' %}"
    path('contacto/', views.contacto, name='contacto'), #"{% url 'contacto' %}"
    path('productos/', views.productos, name='productos'), #"{% url 'productos' %}"
    path('servicios/', views.servicios, name='servicios'), #"{% url 'servicios' %}"
    
    #Login y registro de personas
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'), #"{% url 'crear_usuario' %}"
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'), #"{% url 'iniciar_sesion' %}"
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),  # "{% url 'cerrar_sesion' %}"

    #Carrito de compras
    path('crear_carrito_de_compras/', views.crear_carrito_de_compras, name='crear_carrito_de_compras'),#"{% url 'crear_carrito_de_compras' %}"

    #CRUD de productos
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'), #"{% url 'registrar_producto' %}"
    path('ver_producto/', views.ver_producto, name='ver_producto'), #"{% url 'ver_producto' %}"
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto'), #"{% url 'editar_producto' %}"
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'), #"{% url 'eliminar_producto' %}"

]

