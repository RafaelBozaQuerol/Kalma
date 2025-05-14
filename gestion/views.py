# gestion/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Cliente, Servicio, Visita
from .forms import ClienteForm, ServicioForm, VisitaForm

# Página de inicio
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige a la página principal
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login después de hacer logout

# Vistas de Clientes
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'form_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'form_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('clientes')

# Vistas de Servicios
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'form_servicio.html', {'form': form})

def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'form_servicio.html', {'form': form, 'servicio': servicio})

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('servicios')

# Vistas de Visitas
def visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'visitas.html', {'visitas': visitas})

def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitas')
    else:
        form = VisitaForm()
    return render(request, 'form_visita.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'form_visita.html', {'form': form, 'visita': visita})

def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    visita.delete()
    return redirect('visitas')
