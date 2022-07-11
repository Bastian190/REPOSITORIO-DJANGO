from django import forms
from django.forms import ModelForm
from .models import Periferico
from .models import Contacto
from django.contrib.auth.models import User
class PerifericoForm(ModelForm):
    class Meta:
        model = Periferico
        fields = [ 'idperiferico','marca','modelo','nombre','precio','tipo_periferico','imagen']

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class UseerForm(forms.Form):
    
    username = forms.CharField(
        label="Nombre de usuario", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password_one = forms.CharField(
        label="Password", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(
        label="Confirmar password", widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El nombre de usuario ya existe')


def clean_email(self):
    email = self.cleaned_data['email']
    try:
        u = User.objects.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('Email ya registrado')


def clean_password_two(self):
    password_one = self.cleaned_data['password_one']
    password_two = self.cleaned_data['password_two']
    if password_one == password_two:
        pass
    else:
        raise forms.ValidationError('Password no coinciden')

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))