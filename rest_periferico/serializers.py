from rest_framework import serializers
from Ventasgamer.models import Periferico

class PerifericoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periferico
        fields = [ 'idperiferico','marca','modelo','nombre','precio','tipo_periferico']

