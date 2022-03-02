from django.db import models

# Create your models here.

# Modelo para el comprador
class Comprador(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)

    # Funcion usada para retornar 
    # el nombre del comprador
    def get_name(self):
        return self.nombre + " "

