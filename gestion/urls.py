# gestion/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Rutas de clientes
    path('clientes/', views.clientes, name='clientes'),
    path('cliente/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('cliente/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    # Rutas de servicios
    path('servicios/', views.servicios, name='servicios'),
    path('servicio/nuevo/', views.nuevo_servicio, name='nuevo_servicio'),
    path('servicio/<int:id>/editar/', views.editar_servicio, name='editar_servicio'),
    path('servicio/<int:id>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),

    # Rutas de visitas
    path('visitas/', views.visitas, name='visitas'),
    path('visita/nueva/', views.nueva_visita, name='nueva_visita'),
    path('visita/<int:id>/editar/', views.editar_visita, name='editar_visita'),
    path('visita/<int:id>/eliminar/', views.eliminar_visita, name='eliminar_visita'),
]
