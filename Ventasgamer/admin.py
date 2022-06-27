from django.contrib import admin
from .models import Tipo_periferico,Periferico,Usuario,Contacto
# Register your models here.
admin.site.register(Tipo_periferico)
admin.site.register(Periferico)
admin.site.register(Usuario)
admin.site.register(Contacto)