from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactoModel, PersonaModel, ProductoModel


###### Se creó un formulario de contacto con errores personalizados para practicar lo visto en clase ######
class ContactoForm(forms.ModelForm):
    telefono_cliente = forms.IntegerField()
    
    def clean_nombre_del_cliente(self):
        nombre = self.cleaned_data['nombre_del_cliente']
        if not nombre.replace(' ', '').isalpha():
            raise ValidationError('El nombre debe contener solo letras y espacios.')
        return nombre

    def solo_caracteres(self, value):
        if any(char.isdigit() for char in value):
            raise ValidationError('El nombre no puede contener números.', code='Invalid')

    def clean_telefono_cliente(self):
        telefono = self.cleaned_data['telefono_cliente']
        if len(str(telefono)) < 10:
            raise ValidationError('El número de teléfono debe tener al menos 10 dígitos.')
        return telefono
    
    def clean_mensaje(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data

    class Meta:
        model=ContactoModel
        fields=("nombre_del_cliente","email_cliente","telefono_cliente","consulta")
        widgets = {
            "nombre_del_cliente":forms.TextInput(),
            "email_cliente":forms.EmailInput(),
            "telefono_cliente":forms.NumberInput(),
            "consulta":forms.Textarea(),
        }


#### Modelos de usuario y de persona para crear formularios de inicio de sesion y datos de los clientes ######

class UserRegistrationForm(UserCreationForm):
    nombre_form = forms.CharField(max_length=100)
    apellido_form = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()
    dni = forms.IntegerField()
    fecha_de_nacimiento = forms.DateField()
    direccion_particular = forms.CharField(max_length=200)
    ciudad = forms.CharField(max_length=100)
    codigo_postal = forms.IntegerField()
    telefono = forms.IntegerField()
    CUIT = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    class Meta:
        model=User
        fields=('username','password1', 'password2', 'first_name', 'last_name', 'edad', 'email', 'dni', 'fecha_de_nacimiento', 'direccion_particular', 'ciudad', 'codigo_postal', 'telefono', 'CUIT')
    

#### Modelos de productos para crear formularios de los productos ofrecidos ######

class ProductoForm(forms.ModelForm):
    en_stock = forms.BooleanField(required=False)
    en_oferta = forms.BooleanField(required=False)

    class Meta:
        model=ProductoModel
        fields='__all__'