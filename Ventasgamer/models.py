
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
    idperiferico = models.IntegerField(primary_key=True,verbose_name='Idperiferico',default="Some String")
    marca = models.CharField(max_length=20,verbose_name='Marca',default="Some String")
    modelo = models.CharField(max_length=20,null=True, blank=True, verbose_name='Modelo')
    nombre = models.CharField(max_length=20,null=True, blank=True, verbose_name='Nombre')
    precio = models.CharField(max_length=20,null=True, blank=True,verbose_name='Precio')
    tipo_periferico = models.ForeignKey(Tipo_periferico, on_delete=models.CASCADE)

    def __str__(self):
        return self.idperiferico

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    correo = models.CharField('Correo', max_length=50)
    contrasenna = models.CharField('Contraseña', max_length=50)
    nombreUsuario = models.CharField(max_length=20,null=True, blank=True,verbose_name='Nombre')
    
    def __str__(self):
        return '{0},{1},{2}'.format(self.correo,self.contrasenna,self.nombreUsuario)

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()


    def __str__(self):
        return self.nombre
   