from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# Vista de login de la aplicacion
def login(request):
    template = loader.get_template('login/login.html')
    context = {}
    return HttpResponse(template.render(context,request))

# Vista del registro de la aplicacion 
def registro(request):
    template = loader.get_template('login/registro.html')
    context = {}
    return HttpResponse(template.render(context,request))

# Vista del home de la aplicacion
def home(request):
    template = loader.get_template('productos/home.html')
    context = {}
    return HttpResponse(template.render(context,request))