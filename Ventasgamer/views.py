from django.shortcuts import render, redirect
from .models import Periferico
from .forms import PerifericoForm, ContactoForm, UseerForm,LoginForm
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
    productos = Periferico.objects.all()
    data = {
        'entity': productos
    }
    return render (request, 'Ventasgamer/InterfazMonitores.html', data)



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
    return render(request,'Ventasgamer/interfazMonitores', datos)

# 

def registro(request):
    datos = {
        'forma': UseerForm()
    }

    if(request.method == 'POST'):
        formulario = UseerForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            email = formulario.cleaned_data['email']
            password_one = formulario.cleaned_data['password_one']
            password_two = formulario.cleaned_data['password_two']
            u = User.objects.create_user(
                username=usuario, email=email, password=password_one)
            u.save()
            datos['mensaje'] = 'registro exitoso'
        else:
            print(formulario.errors)
    return render(request, 'Ventasgamer/registro.html', datos)
    
    
def logiin (request):
    datos ={
        'ini': LoginForm()
    }
    if (request.method == 'POST'):
        usu1 = request.POST.get('username')
        u = User.objects.get(username=usu1)
        pas= request.POST.get('password')
        token = Token.objects.get(user=u )
        user = authenticate(request, username=usu1, password=pas, token=token)
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
        
        return render(request,'musica/index.html')

def tienda(request):
    productos = Periferico.objects.all()
    data = {
        'enity' : productos
    }
    return render (request, 'Ventasgamer/shop.html', data)