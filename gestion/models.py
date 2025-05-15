from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Empresa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="empresa")
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="clientes", null=True, blank=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="servicios", null=True, blank=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion_min = models.IntegerField()

    def __str__(self):
        return self.nombre


class Visita(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="visitas", null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    servicios = models.ManyToManyField(Servicio)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Visita de {self.cliente.nombre} el {self.fecha.strftime('%d/%m/%Y')}"
    
    def total(self):
        return sum(servicio.precio for servicio in self.servicios.all())
