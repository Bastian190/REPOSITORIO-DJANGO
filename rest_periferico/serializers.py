from rest_framework import serializers
from Ventasgamer.models import Periferico, Usuario

class PerifericoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periferico
        fields = [ 'idperiferico','marca','modelo','nombre','precio','tipo_periferico']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [ 'id','correo','contrasenna','nombreUsuario']

