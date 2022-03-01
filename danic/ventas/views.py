from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# Vista para el inicio de la aplicacion
def login(request):
    template = loader.get_template('login/login.html')
    context = {}
    return HttpResponse(template.render(context,request))
