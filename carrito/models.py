from django.db import models

# Create your models here.

class Product(models.Model):
    Producto = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Cantidad = models.PositiveIntegerField()
    Imagen = models.CharField(max_length=200, blank=True, default='https://www.webempresa.com/foro/wp-content/uploads/wpforo/attachments/3200/318277=80538-Sin_imagen_disponible.jpg')
    Total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.Producto