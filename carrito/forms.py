from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('Producto', 'Descripcion', 'Precio', 'Cantidad', 'Imagen', 'Total')

# class ContactForm(forms.Form):
#     name = forms.CharField(label='Nombre')
#     email = forms.EmailField(label='Correo electrónico')
#     message = forms.CharField(label='Mensaje', widget=forms.Textarea)
    