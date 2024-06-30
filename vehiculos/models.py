from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    disponible = models.BooleanField(default=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    numero_identidad = models.CharField(max_length=100)
    vehiculo_preferencia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre