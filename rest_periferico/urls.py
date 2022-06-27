from django.urls import path
from rest_periferico.views import lista_periferico, detalle_periferico,UsuarioList
from rest_periferico.viewsLogin import login

urlpatterns = [
    path('lista_periferico',lista_periferico,name="lista_periferico"),
    path('detalle_periferico/<pat>',detalle_periferico,name="detalle_periferico"),
    path('UsuarioList',UsuarioList,name="UsuarioList"),
    path('Login',login,name='Login'),
]