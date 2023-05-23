from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

#from publica.forms import ContactoForm

from datetime import datetime
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from core.forms import ContactoForm

# Create your views here.


def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())

def productos(request):
    template = loader.get_template('core/productos.html')
    return HttpResponse(template.render())

def servicios(request):
    template = loader.get_template('core/servicios.html')
    return HttpResponse(template.render())

def contacto(request):
    template = loader.get_template('core/contacto.html')
    return HttpResponse(template.render())

# def contacto(request):#esta app importa ContactoForm y envía un mail    
#     # mensaje=None
#     if(request.method=='POST'):
#         contacto_form = ContactoForm(request.POST)    
#         # mensaje='Hemos recibido tus datos'
#         # acción para tomar los datos del formulario
#         if(contacto_form.is_valid()):  
#             messages.success(request,'Hemos recibido tus datos')
#             mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
#             mensaje_html=f"""
#                 <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
#                 <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
#                 <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
#             """
#             asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
#             send_mail(
#                 asunto,
#                 mensaje,
#                 settings.EMAIL_HOST_USER,
#                 [settings.RECIPIENT_ADDRESS],
#                 fail_silently=False,
#                 html_message=mensaje_html
#             )          
#         # acción para tomar los datos del formulario
#         else:
#             messages.warning(request,'Por favor revisa los errores en el formulario')
#     else:
#         contacto_form = ContactoForm()

#     context = {                                
#                 'contacto_form':contacto_form
#             }
#     return render(request,'core/contacto.html',context)
