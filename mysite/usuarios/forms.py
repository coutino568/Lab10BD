from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Atributos_extra


class UserForm(ModelForm):
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

class AuthenticationAddForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)

class AddAtributosExtraForm(forms.Form):
    nombre_artistico = forms.CharField(label="Nombre Artistico", max_length=150)

    class Meta:
        model = Atributos_extra
        fields = ['nombre_artistico']
