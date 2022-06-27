from django import forms
from django.forms import ModelForm
from .models import Periferico
from .models import Contacto
from django.contrib.auth.models import User
class PerifericoForm(ModelForm):
    class Meta:
        model = Periferico
        fields = [ 'idperiferico','marca','modelo','nombre','precio','tipo_periferico']

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class UsuarioForm( ModelForm):
    class Meta:
        model = User
        fields = ['username','password']