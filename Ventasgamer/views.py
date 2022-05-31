from django.shortcuts import render, redirect
from .models import Periferico
from .forms import PerifericoForm

# Create your views here.
def home(request):

    return render(request,'Ventasgamer/index.html')


def contacto(request):
    return render(request,'Ventasgamer/Contacto.html')

def monitores(request):
    return render(request,'Ventasgamer/InterfazMonitores.html')

def login(request):
    return render(request,'Ventasgamer/Login.html')

def registro(request):
    return render(request,'Ventasgamer/registro.html')




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
