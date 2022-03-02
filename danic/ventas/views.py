from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

from .models import Comprador
from .forms import CustomUserCreationForm

# Create your views here.

# Vista para autenticacion

# Vista de login de la aplicacion
def login(request):
    template = loader.get_template('registration/login.html')
    context = {}
    return HttpResponse(template.render(context,request))


# Vista del registro de la aplicacion 
def registro(request):
    template = loader.get_template('registration/registro.html')
    data = { 'form': CustomUserCreationForm  }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.succes(request, "Usuario registrado correctamente")
            return redirect('home') # redirige el home
    
    return HttpResponse(template.render(data,request))


# Vista del home de la aplicacion
def home(request):
    template = loader.get_template('productos/home.html')
    context = {}
    return HttpResponse(template.render(context,request))