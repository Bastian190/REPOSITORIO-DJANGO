from django import forms
from django.forms import ModelForm
from .models import Periferico

class PerifericoForm(ModelForm):
    class Meta:
        model = Periferico
        fields = [ 'idperiferico','marca','modelo','nombre','precio','tipo_periferico']

