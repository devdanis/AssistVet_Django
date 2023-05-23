from django.urls import path
from . import views

urlpatterns = [
    #Crear links para crear/leer/modificar/eliminar empleado
    path('administrador_empleados/', views.Administrador_empleados, name='administrador_empleados'), #"{% url 'administrador_empleados' %}"
    path('administrador_empleados_crear_empleado/', views.Administrador_empleados_crear_empleado.as_view(), name='administrador_empleados_crear_empleado'), #"{% url 'administrador_empleados_crear_empleado' %}"
    path('administrador_empleados_leer_empleado/', views.Administrador_empleados_leer_empleado.as_view(), name='administrador_empleados_leer_empleado'), #"{% url 'administrador_empleados_leer_empleado' %}"
    path('administrador_empleados_modificar_empleado/<int:pk>', views.Administrador_empleados_modificar_empleado.as_view(), name='administrador_empleados_modificar_empleado'), #"{% url 'administrador_empleados_modificar_empleado' %}"
    path('administrador_empleados_eliminar_empleado/<int:pk>', views.Administrador_empleados_eliminar_empleado.as_view(), name='administrador_empleados_eliminar_empleado'), #"{% url 'administrador_empleados_eliminar_empleado' %}"

    #Crear links para crear/leer/modificar/eliminar productos
    path('administrador_productos/', views.Administrador_productos, name='administrador_productos'), #"{% url 'administrador_productos' %}"
    path('administrador_productos_crear_producto/', views.Administrador_productos_crear_producto, name='administrador_productos_crear_producto'), #"{% url 'administrador_productos_crear_producto' %}"
    path('administrador_productos_leer_producto/', views.Administrador_productos_leer_producto, name='administrador_productos_leer_producto'), #"{% url 'administrador_productos_leer_producto' %}"
    path('administrador_productos_modificar_producto/', views.Administrador_productos_modificar_producto, name='administrador_productos_modificar_producto'), #"{% url 'administrador_productos_modificar_producto' %}"
    path('administrador_productos_eliminar_producto/', views.Administrador_productos_eliminar_producto, name='administrador_productos_eliminar_producto'), #"{% url 'administrador_productos_eliminar_producto' %}"

    #Crear links para leer/registrar un pedido a proveedor/registrar en caja una compra/hacer un pedido a  un delivery
    path('empleado_caja1/', views.Empleado_caja1, name='empleado_caja1'), #"{% url 'empleado_caja1' %}"
]