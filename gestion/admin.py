from django.contrib import admin
from .models import Cliente, Servicio, Visita

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Visita)