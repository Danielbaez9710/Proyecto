from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
   # path('', views.home, name="home"),
    path('login/registro',views.registro, name="registro"),
]
