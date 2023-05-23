from django import forms

from .models import Empleado#, Producto

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model=Empleado
        fields='__all__'

        nombre=forms.CharField(
        label='nombre', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un nombre'})
        )

        apellido=forms.CharField(
        label='apellido', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un apellido'})
        )

        edad=forms.CharField(
        label='edad', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese la edad'})
        )

        email = forms.EmailField(
            label='email',
            max_length=100,
            required=True,
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'type':'email'})
        )

        DNI=forms.CharField(
        label='DNI', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un DNI'})
        )

        fecha_de_nacimiento=forms.CharField(
        label='fecha_de_nacimiento', 
        widget=forms.DateInput(attrs={'placeholder':'Ingrese una Fecha de Nacimiento','type':'date'})
        )

        nombre_de_usuario=forms.CharField(
        label='nombre_de_usuario', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un Nombre de Usuario'})
        )

        contrasenia=forms.CharField(
        label='contrasenia', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese una Contraseña', 'type':'password'})
        )

        CUIT=forms.CharField(
        label='CUIT', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un C.U.I.T.'})
        )

        duenio = forms.BooleanField(
        label='duenio',
        widget=forms.CheckboxInput(attrs={'value':0})
        )

        empleado = forms.BooleanField(
        label='empleado',
        widget=forms.CheckboxInput(attrs={'value':1})
        )

        medico_veterinario = forms.BooleanField(
        label='medico_veterinario',
        widget=forms.CheckboxInput(attrs={'value':0})
        )

        direccion_particular=forms.CharField(
        label='direccion_particular', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese una dirección'})
        )

        ciudad=forms.CharField(
        label='Ciudad', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese una Ciudad'})
        )

        codigo_postal=forms.CharField(
        label='codigo_postal', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un codigo postal'})
        )

        telefono=forms.CharField(
        label='telefono', 
        widget=forms.TextInput(attrs={'placeholder':'Ingrese un Cel./Tel.'})
        )

