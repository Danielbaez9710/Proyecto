from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('registration/registro', views.registro, name="registro"),
    path('productos/home', views.home, name="home"),
]
