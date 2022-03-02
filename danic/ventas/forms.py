from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Modelos
from .models import Comprador

# Crear formulario para Comprador
class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
