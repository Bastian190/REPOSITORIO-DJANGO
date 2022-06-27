from django.urls import path, include
from .views import home, contacto, monitores, logiin, registro, Lista
from .views import form_periferico, modificar_Periferico, eliminar_Periferico
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',home,name="home"),
    path('contacto/', contacto, name="contacto"),
    path('monitores',monitores,name="monitores"),
    path('login',logiin,name="login"),
    path('registro',registro,name="registro"),
    path('agregar_Periferico',form_periferico,name="agregar_Periferico"),
    path('modificar_periferico/<id>',modificar_Periferico,name="modificar_periferico"),
    path('eliminar_periferico/<id>',eliminar_Periferico,name="eliminar_periferico"),
    path('lista',Lista,name="lista"),
    path('logout', LogoutView.as_view()),
    path('accounts/', include('allauth.urls')),
]
