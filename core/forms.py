from django import forms
from django.forms import ValidationError

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

class ContactoForm(forms.Form):

    # TIPO_CONSULTA = (
    #     ('','-Seleccione el motivo de su consulta-'),
    #     (1,'Turnos de la Veterinaria'),
    #     (2,'Precio de Servicios'),
    #     (3,'No encuentro un producto'),
    #     (4,'Otro'),
    # )

    # TIPO_RESPUESTA_PREFERIDA = (
    #     ('','-Quiere que Asist Vet se contacte con Ud mediante...-'),
    #     (1,'E-Mail'),
    #     (2,'Teléfono'),
    # )

    nombre = forms.CharField(
            label='nombre_de_cliente', 
            max_length=50,
            validators=(solo_caracteres,),
            widget=forms.TextInput(
                    attrs={'class':'######',
                        'placeholder':'Solo letras'}
                    )
        )
    
    # tipo_consulta = forms.ChoiceField(
    #     label='Tipo de consulta',
    #     choices=TIPO_CONSULTA,
    #     widget=forms.Select(attrs={'class':'######'})
    # )

    # asunto = forms.CharField(
    #     label='Asunto',
    #     max_length=100,
    #     widget=forms.TextInput(attrs={'class':'######'})
    # )


    mensaje = forms.CharField(
        label='consulta',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'######'})
    )


    # tipo_respuesta = forms.ChoiceField(
    #     label='Respuesta',
    #     choices=TIPO_RESPUESTA_PREFERIDA,
    #     widget=forms.Select(attrs={'class':'######'})
    # )

    email = forms.EmailField(
            label='email-cliente',
            required=True,
            max_length=100,
            #validators=(validate_email),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'class':'######','type':'email'})
        )
    
    telefono = forms.EmailField(
            label='telefono_cliente',
            required=True,
            max_length=100,
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'class':'######','type':'number'})
        )
    

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
