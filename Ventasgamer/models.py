
from operator import truediv
from tabnanny import verbose
from django.db import models

# Create your models here.
class Tipo_periferico(models.Model):
    idTipo = models.IntegerField(primary_key=True,verbose_name='Id Tipo')
    nombreTipo = models.CharField(max_length=50,verbose_name='Nombre del Tipo')

    def __str__(self):
        return self.nombreTipo

class Periferico(models.Model):
    idperiferico = models.CharField(max_length=6,primary_key=True, verbose_name='Idperiferico')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20,null=True, blank=True, verbose_name='Modelo')
    nombre = models.CharField(max_length=20,null=True, blank=True, verbose_name='Nombre')
    precio = models.CharField(max_length=20,null=True, blank=True,verbose_name='Precio')
    tipo_periferico = models.ForeignKey(Tipo_periferico, on_delete=models.CASCADE)

    def __str__(self):
        return self.idperiferico
