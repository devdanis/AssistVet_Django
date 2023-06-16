from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

def validate_email(value):
    email_validator = EmailValidator(message='Ingrese una dirección de correo electrónico válida.')
    try:
        email_validator(value)
    except ValidationError as e:
        raise ValidationError(e.messages)

class ContactoModel(models.Model):
    
    LEIDO=[(1,'No leido'), (2,'Leido')]

    nombre_del_cliente = models.CharField(max_length=100,verbose_name='Nombre del cliente')
    email_cliente = models.EmailField(max_length=150,null=True, validators=[validate_email])
    telefono_cliente = models.IntegerField(verbose_name="Teléfono del cliente")
    consulta= models.TextField(max_length=1000,verbose_name='Consulta del cliente')
    fecha_contacto=models.DateTimeField(auto_now_add=True)
    leido=models.IntegerField(choices=LEIDO, default=1)

    def __str__(self):
        return f"Nombre del cliente: {self.nombre_del_cliente}"
    
    class Meta():
        verbose_name_plural = 'Contactos'
        db_table = 'Contacto'

    def clean_nombre_del_cliente(self):
        nombre = self.cleaned_data['nombre_del_cliente']
        if not nombre.replace(' ', '').isalpha():
            raise ValidationError('El nombre debe contener solo letras y espacios.')
        return nombre

class PersonaModel(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombre', blank=True, null=True)
    apellido = models.CharField(max_length=150, verbose_name='Apellido', blank=True, null=True)
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    fecha_de_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento",null=True,default=None)
    direccion_particular = models.CharField(max_length=100,verbose_name='Direccion Particular')
    ciudad = models.CharField(max_length=100,verbose_name='Ciudad de Residencia')
    codigo_postal = models.CharField(max_length=12,verbose_name='Código Postal')
    telefono = models.IntegerField(verbose_name="Cel./Tel.")
    CUIT = models.IntegerField(verbose_name="C.U.I.T.")
    #productos=models.ManyToManyField(ProductoModel,through='Carrito_de_ComprasModel')
    def __str__(self):
        return f"Usuario: {self.user.first_name}-{self.user.last_name}-{self.user.username}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    '''
    '''
    class Meta():
        verbose_name_plural = 'Personas'
        db_table = 'Personas'

class ProductoModel(models.Model):
    id_producto=models.AutoField(primary_key=True)

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
    peso_del_animal=models.CharField(max_length=50, verbose_name="Peso del Animal", default='Ítem')
    edad_del_animal=models.IntegerField(verbose_name="Edad del Animal", default='N/C')
    descripcion=models.TextField(verbose_name="Descripción del Producto")
    precio_de_compra=models.IntegerField(verbose_name="Precio de compra", default=0)
    margen_de_ganancias=models.IntegerField(verbose_name="Margen de ganancias", default=2)
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
        return f"Producto: {self.marca} {self.descripcion} {self.unidad}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Productos'
        db_table = 'Productos'

class Carrito_de_ComprasModel(models.Model):
    id_producto = models.ForeignKey(ProductoModel,on_delete=models.CASCADE)
    username = models.ForeignKey(PersonaModel,on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Carritos de compra'
        db_table = 'Carrito de Compra'