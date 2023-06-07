from django.db import models

# Create your models here.

class ProductosTienda(models.Model):
    Nombre = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen = models.CharField(max_length=200, blank=True, default='https://www.webempresa.com/foro/wp-content/uploads/wpforo/attachments/3200/318277=80538-Sin_imagen_disponible.jpg')

    def __str__(self):
        return self.Nombre