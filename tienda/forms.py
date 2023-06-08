from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from tienda.models import ProductosTienda, Customer
from django.contrib.auth.models import User

class ProductosTiendaForm(forms.ModelForm):
    class Meta:
        model = ProductosTienda
        fields = ('Nombre', 'Precio', 'Imagen')
        
        
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    
class CustomerProfileForm(forms.ModelForm):
    pass

class Meta:
    model = Customer
    fields = ('user', 'name')