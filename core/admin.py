from django.contrib import admin
from core.models import ContactoModel, PersonaModel, ProductoModel
from django.contrib.auth.admin import UserAdmin



class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre_del_cliente","email_cliente","telefono_cliente","consulta","fecha_contacto","leido",)
    list_editable = ("leido",)
    list_filter = ("nombre_del_cliente","fecha_contacto")
    search_fields = ("nombre_del_cliente",)
    exclude = ("leido",)

#class PersonaAdmin(UserAdmin):
#    list_display=("user","first_name", "last_name")

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "edad", "email", "dni", "fecha_de_nacimiento", "direccion_particular", "ciudad", "codigo_postal", "telefono", "CUIT")
'''
    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name
'''
class ProductoAdmin(admin.ModelAdmin):
    list_display=("tipo_de_producto", "marca", "unidad")

# Register your models here.

admin.site.register(ContactoModel, ContactoAdmin)
admin.site.register(PersonaModel, PersonaAdmin)
admin.site.register(ProductoModel, ProductoAdmin)

