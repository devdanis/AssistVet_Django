from django import forms
from tienda.models import ProductosTienda


class ProductosTiendaForm(forms.ModelForm):
    class Meta:
        model = ProductosTienda
        fields = ('Producto', 'Precio', 'Imagen')