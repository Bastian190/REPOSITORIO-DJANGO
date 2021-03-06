from msilib.schema import Class
from winreg import QueryReflectionKey
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Ventasgamer.models import Periferico, Usuario
from rest_periferico.serializers import PerifericoSerializer, UsuarioSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_periferico(request):
    if request.method == 'GET':
        listaPeriferico = Periferico.objects.all()
        serializer = PerifericoSerializer(listaPeriferico, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = PerifericoSerializer(data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_periferico(request, idp):
    try:
        periferico = Periferico.objects.get(idperiferico = idp)
    except Periferico.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializ = PerifericoSerializer(periferico)
        return Response(serializ.data)
    elif request.method == "PUT":
        dataV = JSONParser().parse(request)
        serializ = PerifericoSerializer(periferico, data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        periferico.delete() # DELETE A LA BD
        return Response(status = status.HTTP_204_NO_CONTENT) 


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def UsuarioList(request):
    if request.method == 'GET':
        Usuariol_Lista = Usuario.objects.all()
        serializer = UsuarioSerializer(Usuariol_Lista, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
    
    
    