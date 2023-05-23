from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    fecha_de_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento",null=True,default=None)

class Duenio(Persona):
    nombre_de_usuario = models.CharField(max_length=100,verbose_name='Nombre de Usuario')
    contrasenia= models.CharField(max_length=10,verbose_name='Contraseña')
    CUIT = models.IntegerField(verbose_name="C.U.I.T.")
    duenio1=models.BooleanField(verbose_name="Dueño",default=True)
    empleado1=models.BooleanField(verbose_name="Empleado",default=False)
    medico_veterinario1=models.BooleanField(verbose_name="Médico Veterinario",default=True)
    direccion_particular = models.CharField(max_length=100,verbose_name='Direccion Particular')
    ciudad = models.CharField(max_length=100,verbose_name='Ciudad de Residencia')
    codigo_postal = models.CharField(max_length=12,verbose_name='Código Postal')
    telefono = models.IntegerField(verbose_name="Cel./Tel.")

    def __str__(self):
        return f"Dueño: {self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Duenios'

class Empleado(Persona):
    nombre_de_usuario = models.CharField(max_length=100,verbose_name='Nombre de Usuario')
    contrasenia= models.CharField(max_length=10,verbose_name='Contraseña')
    CUIT = models.IntegerField(verbose_name="C.U.I.T.")
    duenio2=models.BooleanField(verbose_name="Dueño",default=True)
    empleado2=models.BooleanField(verbose_name="Empleado",default=False)
    medico_veterinario2=models.BooleanField(verbose_name="Médico Veterinario",default=False)
    direccion_particular = models.CharField(max_length=100,verbose_name='Direccion Particular')
    ciudad = models.CharField(max_length=100,verbose_name='Ciudad de Residencia')
    codigo_postal = models.CharField(max_length=12,verbose_name='Código Postal')
    telefono = models.IntegerField(verbose_name="Cel./Tel.")

    def __str__(self):
        return f"Empleado: {self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Empleados'

class Producto(models.Model):
    TIPO_DE_PRODUCTO = [
        (1,'Alimento para Perros'),
        (2,'Alimento para Gatos'),
        (3,'Accesorios'),
        (4,'Juguetes'),
    ]

    UNIDAD_DE_COMPRA = [
        (1,'Ítem'),
        (2,'1 kg'),
        (3,'3 kg'),
        (4,'7 kg'),
        (5,'15 kg'),
    ]

    tipo_de_producto = models.IntegerField(choices=TIPO_DE_PRODUCTO,default=1)
    marca= models.CharField(max_length=50,verbose_name='Marca del Producto')
    unidad = models.IntegerField(choices=UNIDAD_DE_COMPRA,default=1)
    peso_del_animal=models.IntegerField(verbose_name="Peso del Animal", default=0)
    edad_del_animal=models.IntegerField(verbose_name="Edad del Animal", default=0)
    descripcion=models.TextField(verbose_name="Descripción del Producto")
    precio_de_compra=models.IntegerField(verbose_name="Precio de compra", default=0)
    precio_de_venta=models.IntegerField(verbose_name="Precio de venta", default=0)
    en_oferta=models.BooleanField(verbose_name="En oferta 20%",default=False)
    cantidad_en_stock=models.IntegerField(verbose_name="Cantidad en Stock", default=0)
    en_stock=models.BooleanField(verbose_name="En Stock",default=False)
    alerta_bajo_stock=models.IntegerField(verbose_name="Alerta de Cantidad Baja en Stock", default=10)#me alerta si voy a tener que hacer un pedido
    imagen_producto = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Imagen del Producto')
    nombre_del_proveedor=models.TextField(verbose_name="Nombre completo del proveedor")
    contacto_del_proveedor=models.TextField(verbose_name="Nombre completo del contacto del proveedor")
    telefono_proveedor = models.IntegerField(verbose_name="Cel./Tel. del Proveedor")
    email_proveedor = models.EmailField(max_length=150,null=True)

    def __str__(self):
        return f"Prpducto: {self.marca} {self.descripcion} {self.unidad}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Productos'
