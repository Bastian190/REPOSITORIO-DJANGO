from django.shortcuts import render, redirect
from .models import Periferico
from .forms import PerifericoForm, ContactoForm, UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):

    return render(request,'Ventasgamer/index.html')
def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    return render (request, 'Ventasgamer/contacto.html', data)




def monitores(request):
    return render(request,'Ventasgamer/InterfazMonitores.html')





def form_periferico(request):
    datos = {
        'form' :  PerifericoForm()
    }

    if (request.method == 'POST'):
        formulario = PerifericoForm(request.POST)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = 'Periferico se guardó'
        else:
            datos['mensaje'] = 'Periferico NO se guardó'
  
    return render(request,'Ventasgamer/agregar_periferico.html',datos)

def modificar_Periferico(request, id):
    periferico = Periferico.objects.get(idperiferico=id)

    datos = {
        'form': PerifericoForm(instance=periferico)
    }

    if (request.method == 'POST'):
        formulario = PerifericoForm(data=request.POST, instance=periferico)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = 'Periferico se modificó'
        else:
            datos['mensaje'] = 'Periferico NO se modificó'

    return render(request,'Ventasgamer\modificar_periferico.html', datos)

def eliminar_Periferico(request, id):
    periferico = Periferico.objects.get(idperiferico=id)
    periferico.delete() 

    return redirect(to='lista')

def Lista(request):
    periferico = Periferico.objects.all()
    datos = {
        'Periferico':periferico
    }
    return render(request,'Ventasgamer/Lista_perifericos.html', datos)

# 

def registro(request):
    datos ={
        'forma':UsuarioForm()
    }

    if(request.method == 'POST'):
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()            
            datos['mensaje'] = 'registro exitoso'
        else:
            print(formulario.errors)
    return render(request, 'Ventasgamer/registro.html', datos)
    
def logiin (request):
    datos ={
        'ini': UsuarioForm()
    }
    if (request.method == 'POST'):
        token = Token()
        usu1 = request.POST.get('username')
        pas= request.POST.get('password')
        user = authenticate(request, username=usu1, password=pas)
        if user is not None:
            login(request, user)
            datos['mensaje']='inicio exitoso'
        else:
            print(usu1, pas)
    return render(request,'Ventasgamer/login.html', datos)

def logout (request):
    usu1 = request.POST.get('username')
    pas= request.POST.get('password')
    user = authenticate(request, username=usu1, password=pas)
    if user is not None:
        logout(request, user)
        
        return render(request,'Ventasgamer/index.html')


