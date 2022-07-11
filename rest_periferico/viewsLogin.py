from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from Ventasgamer.forms import LoginForm

@api_view(['POST'])
def login(request):
    data = LoginForm(request.POST)
    v_username = data['username']
    v_password = data['password']
    try:
        usuario = User.objects.get(username = v_username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")
    
    pass_valido = check_password(v_password, usuario.password)
    
    if not pass_valido:
        return Response("Password Incorrecta")
    
    token, created = Token.objects.get_or_create(user=usuario)
    return Response(token.key)
    