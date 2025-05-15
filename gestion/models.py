from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion_min = models.IntegerField()

    def __str__(self):
        return self.nombre

class Visita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    servicios = models.ManyToManyField(Servicio)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Visita de {self.cliente.nombre} el {self.fecha.strftime('%d/%m/%Y')}"
    
    def total(self):
        total_precio = sum(servicio.precio for servicio in self.servicios.all())
        return total_precio