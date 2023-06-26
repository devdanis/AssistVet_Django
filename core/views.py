from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings

from datetime import datetime
from django.contrib import messages

from django.conf import settings
from core.forms import ContactoForm, UserRegistrationForm, ProductoForm
from core.models import PersonaModel, ProductoModel, Carrito_de_ComprasModel
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from decimal import Decimal
# Create your views here.


################ Lógica de Negocios de las paginas "comunes" ###################


def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())

def productos(request):
    template = loader.get_template('core/productos.html')
    return HttpResponse(template.render())

def servicios(request):
    template = loader.get_template('core/servicios.html')
    return HttpResponse(template.render())


############## Lógica de Negocios de la pagina de 'contacto' que tiene un formulario que se envía a una base de datos #################


def contacto(request):
    if request.method == 'POST':
        #print(request.POST)
        contactoform = ContactoForm(request.POST)
        if contactoform.is_valid():
            contactoform.save()
            messages.success(request, '¡¡¡Formulario enviado exitosamente!!!')
            return redirect('contacto')
        else:
            # Agregar los mensajes de error al formulario
            for field, errors in contactoform.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            #print(contactoform.errors)
    else:
        contactoform = ContactoForm()

    return render(request, 'core/contacto.html', {'contactoform': contactoform})



################ Lógica de Negocios de las paginas relativas al inicio de sesión y la creacion de usuarios ###################



def crear_usuario(request):
    if request.method == 'POST':
        #print(request.POST)
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nombre_form']
            user.last_name = form.cleaned_data['apellido_form']
            user.save()

            persona = PersonaModel(
                user=user,
                nombre=form.cleaned_data['nombre_form'],
                apellido=form.cleaned_data['apellido_form'],
                edad=form.cleaned_data['edad'],
                email=form.cleaned_data['email'],
                dni=form.cleaned_data['dni'],
                fecha_de_nacimiento=form.cleaned_data['fecha_de_nacimiento'],
                direccion_particular=form.cleaned_data['direccion_particular'],
                ciudad=form.cleaned_data['ciudad'],
                codigo_postal=form.cleaned_data['codigo_postal'],
                telefono=form.cleaned_data['telefono'],
                CUIT=form.cleaned_data['CUIT']
            )
            persona.save()
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente.')
            #print('Usuario creado exitosamente.')
            return redirect('iniciar_sesion')  # Cambia 'iniciar_sesion' por la URL de la página de inicio de sesión de tu aplicación

        else:
            messages.error(request, 'Error al crear el usuario. Revise los campos.')
            #print('Error al crear el usuario. Revise los campos.')
            #print(form.errors)

    else:
        form = UserRegistrationForm()
    return render(request, 'core/crear_usuario.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is not None and nxt == 'crear_carrito_de_compras':
                return redirect('crear_carrito_de_compras')
            else:
                return redirect('productos')
        else:
            messages.error(request, 'Cuenta o contraseña incorrecta, inicie sesión correctamente')
    return render(request, 'core/iniciar_sesion.html', {'title': 'Iniciar sesión'})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')



################ Lógica de Negocios de las paginas relativas al CRUD de los productos que ofrece la veterinaria ###################



def registrar_producto(request):
    if request.method == 'POST':
        #print(request.POST)
        #print(request.FILES)  # Imprime los archivos subidos en la consola
        form = ProductoForm(request.POST, request.FILES) # Asegúrate de agregar request.FILES para procesar los archivos subidos
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            #print("Archivos subidos:", request.FILES)  # Imprime los archivos subidos en la consola
            return redirect('index')
        #else:
            #print("Errores en el formulario:", form.errors)  # Imprime los errores del formulario en la consola
    else:
        form = ProductoForm()

    return render(request, 'core/registrar_producto.html', {'registrar_producto': form})

def ver_producto(request):
    tipos_de_producto = ProductoModel.objects.values_list('tipo_de_producto', flat=True).distinct()
    marcas = ProductoModel.objects.values_list('marca', flat=True).distinct()
    
    tipo_de_producto = request.GET.get('tipo_de_producto') # Obtener el valor del filtro 'tipo_de_producto' de la URL
    marca = request.GET.get('marca') # Obtener el valor del filtro 'marca' de la URL
    
    productos = ProductoModel.objects.all()
    # Aplicar los filtros si se proporcionan valores válidos
    if tipo_de_producto:
        productos = productos.filter(tipo_de_producto=tipo_de_producto)
    
    if marca:
        productos = productos.filter(marca=marca)
    
    return render(request, 'core/ver_producto.html', {'marcas': marcas,'tipos_de_producto': tipos_de_producto, 'productos': productos})

def editar_producto(request, id_producto):
    producto = get_object_or_404(ProductoModel, pk=id_producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el producto correctamente')
            return redirect('ver_producto')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'core/editar_producto.html', {'formulario': form})

def eliminar_producto(request, id_producto):
    try:
        producto = ProductoModel.objects.get(pk=id_producto)
    except ProductoModel.DoesNotExist:
        return render(request, 'core/404_admin.html')
    
    messages.success(request, 'Se ha eliminado el producto correctamente')          
    producto.delete()
    
    return redirect('ver_producto')

################ Lógica de Negocios de la creación del "carrito de compras"  ###################
################ En desarrollo  ###################

# @login_required
# def crear_carrito_de_compras(request,sender, instance, created, **kwargs):
#     if request.user.is_authenticated:
#         user = request.user
#         # Obtén el usuario actual
#         if created:
#             PersonaModel.objects.create(user=instance)
        
        

#         # Verifica si el usuario tiene un registro en el modelo Carrito_de_ComprasModel
#         carrito = Carrito_de_ComprasModel.objects.filter(username__user=user).first()

#         if not carrito:
#             # Si no existe un registro en Carrito_de_ComprasModel para el usuario, crea uno nuevo
#             carrito = Carrito_de_ComprasModel.objects.create(username=user.personamodel)

#         # Obtén los productos del modelo ProductoModel
#         productos = ProductoModel.objects.all()

#         # Puedes realizar cualquier otra lógica adicional aquí

#         tipos_de_producto = ProductoModel.objects.values_list('tipo_de_producto', flat=True).distinct()
#         marcas = ProductoModel.objects.values_list('marca', flat=True).distinct()
#         unidades = ProductoModel.objects.values_list('unidad', flat=True).distinct()
#         pesos_del_animal = ProductoModel.objects.values_list('pesos_del_animal', flat=True).distinct()
#         edades_del_animal = ProductoModel.objects.values_list('edades_del_animal', flat=True).distinct()
#         en_ofertas = ProductoModel.objects.values_list('en_ofertas', flat=True).distinct()
#         precios_de_venta = ProductoModel.objects.values_list('precios_de_venta', flat=True).distinct()
#         imagenes_producto = ProductoModel.objects.values_list('imagenes_producto', flat=True).distinct()

#         tipo_de_producto = request.GET.get('tipo_de_producto') # Obtener el valor del filtro 'tipo_de_producto' de la URL
#         marca = request.GET.get('marca') # Obtener el valor del filtro 'marca' de la URL
#         unidad = request.GET.get('unidad') # Obtener el valor del filtro 'unidad' de la URL
#         peso_del_animal = request.GET.get('peso_del_animal') # Obtener el valor del filtro 'peso_del_animal' de la URL
#         edad_del_animal = request.GET.get('edad_del_animal') # Obtener el valor del filtro 'edad_del_animal' de la URL
#         en_oferta = request.GET.get('en_oferta') # Obtener el valor del filtro 'en_oferta' de la URL
#         precio_de_venta = request.GET.get('precio_de_venta') # Obtener el valor del filtro 'precio_de_venta' de la URL
#         imagen_producto = request.GET.get('imagen_producto') # Obtener el valor del filtro 'imagen_producto' de la URL

#         productos = ProductoModel.objects.all()
#         # Aplicar los filtros si se proporcionan valores válidos
#         if tipo_de_producto:
#             productos = productos.filter(tipo_de_producto=tipo_de_producto)

#         if marca:
#             productos = productos.filter(marca=marca)

#         if unidad:
#             productos = productos.filter(unidad=unidad)

#         if peso_del_animal:
#             productos = productos.filter(peso_del_animal=peso_del_animal)

#         if edad_del_animal:
#             productos = productos.filter(edad_del_animal=edad_del_animal)

#         if en_oferta:
#             productos = productos.filter(en_oferta=en_oferta)
        
#         if imagen_producto:
#             productos = productos.filter(imagen_producto=imagen_producto)

#         if precio_de_venta:
#             if precio_de_venta == 'ascendente':
#                 productos = productos.order_by('precio_de_venta')
#             elif precio_de_venta == 'descendente':
#                 productos = productos.order_by('-precio_de_venta')
        
#         context = {
#         'productos': productos,
#         'tipos_de_producto': tipos_de_producto,
#         'marcas': marcas,
#         'unidades': unidades,
#         'pesos_del_animal': pesos_del_animal,
#         'edades_del_animal': edades_del_animal,
#         'en_ofertas': en_ofertas,
#         'precios_de_venta': precios_de_venta,
#         'imagenes_producto': imagenes_producto
#         }

#         return render(request, 'core/crear_carrito_de_compras.html', context)
#     else:
#         # Si el usuario no está autenticado, redirige al inicio de sesión o muestra un mensaje de error
#         return redirect('iniciar_sesion')

@login_required
def crear_carrito_de_compras(request):
    user = request.user
    
    # Verifica si el usuario tiene un registro en el modelo PersonaModel
    persona = PersonaModel.objects.filter(user=user).first()

    if not persona:
        # Si no existe un registro en PersonaModel para el usuario, crea uno nuevo
        persona = PersonaModel.objects.create(user=user)

    # Verifica si el usuario tiene un registro en el modelo Carrito_de_ComprasModel
    carrito = Carrito_de_ComprasModel.objects.filter(username__user=user).first()

    if not carrito:
        # Si no existe un registro en Carrito_de_ComprasModel para el usuario, crea uno nuevo
        carrito = Carrito_de_ComprasModel.objects.create(username=persona)

    # Obtén los productos del modelo ProductoModel
    productos = ProductoModel.objects.all()

    # Puedes realizar cualquier otra lógica adicional aquí

    tipos_de_producto = ProductoModel.objects.values_list('tipo_de_producto', flat=True).distinct()
    marcas = ProductoModel.objects.values_list('marca', flat=True).distinct()
    unidades = ProductoModel.objects.values_list('unidad', flat=True).distinct()
    pesos_del_animal = ProductoModel.objects.values_list('pesos_del_animal', flat=True).distinct()
    edades_del_animal = ProductoModel.objects.values_list('edades_del_animal', flat=True).distinct()
    en_ofertas = ProductoModel.objects.values_list('en_ofertas', flat=True).distinct()
    precios_de_venta = ProductoModel.objects.values_list('precios_de_venta', flat=True).distinct()
    imagenes_producto = ProductoModel.objects.values_list('imagenes_producto', flat=True).distinct()

    tipo_de_producto = request.GET.get('tipo_de_producto') # Obtener el valor del filtro 'tipo_de_producto' de la URL
    marca = request.GET.get('marca') # Obtener el valor del filtro 'marca' de la URL
    unidad = request.GET.get('unidad') # Obtener el valor del filtro 'unidad' de la URL
    peso_del_animal = request.GET.get('peso_del_animal') # Obtener el valor del filtro 'peso_del_animal' de la URL
    edad_del_animal = request.GET.get('edad_del_animal') # Obtener el valor del filtro 'edad_del_animal' de la URL
    en_oferta = request.GET.get('en_oferta') # Obtener el valor del filtro 'en_oferta' de la URL
    precio_de_venta = request.GET.get('precio_de_venta') # Obtener el valor del filtro 'precio_de_venta' de la URL
    imagen_producto = request.GET.get('imagen_producto') # Obtener el valor del filtro 'imagen_producto' de la URL

    productos = ProductoModel.objects.all()
    # Aplicar los filtros si se proporcionan valores válidos