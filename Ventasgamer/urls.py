from django.urls import path
from .views import home, contacto, monitores, login, registro, Lista
from .views import form_periferico, modificar_Periferico, eliminar_Periferico




urlpatterns = [
    path('',home,name="home"),
    path('contacto',contacto,name="contacto"),
    path('monitores',monitores,name="monitores"),
    path('login',login,name="login"),
    path('registro',registro,name="registro"),
    path('agregar_Periferico',form_periferico,name="agregar_Periferico"),
    path('modificar_periferico/<id>',modificar_Periferico,name="modificar_periferico"),
    path('eliminar_periferico/<id>',eliminar_Periferico,name="eliminar_periferico"),
    path('lista',Lista,name="lista"),
]
