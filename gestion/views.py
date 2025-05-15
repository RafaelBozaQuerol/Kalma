# gestion/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Cliente, Servicio, Visita, Empresa
from .forms import ClienteForm, ServicioForm, VisitaForm, EmpresaForm

# Página de inicio
def index(request):
    return render(request, "index.html")

@login_required
def crear_empresa(request):
    try:
        # Si el usuario ya tiene empresa, redirigir a alguna página (ejemplo: index)
        if Empresa.objects.filter(user=request.user).exists():
            return redirect('index')
    except:
        pass
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.usuario = request.user
            empresa.save()
            return redirect('index')
    else:
        form = EmpresaForm()
    
    return render(request, 'crear_empresa.html', {'form': form})

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
@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.empresa = Empresa.objects.get(usuario=request.user)
            cliente.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'form_cliente.html', {'form': form})

@login_required
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

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('clientes')

# Vistas de Servicios
@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

@login_required
def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.empresa = Empresa.objects.get(usuario=request.user)
            servicio.save()
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'form_servicio.html', {'form': form})

@login_required
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

@login_required
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('servicios')

# Vistas de Visitas
@login_required
def visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'visitas.html', {'visitas': visitas})

@login_required
def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            visita = form.save(commit=False)
            visita.empresa = Empresa.objects.get(usuario=request.user)
            visita.save()
            form.save_m2m()
            return redirect('visitas')
    else:
        form = VisitaForm()
    return render(request, 'form_visita.html', {
        'form': form, 
        'clientes': Cliente.objects.all(), 
        'servicios': Servicio.objects.all()
        })

@login_required
def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'form_visita.html', {
        'form': form, 
        'visita': visita, 
        'clientes': Cliente.objects.filter(id=visita.cliente.id),
 		'servicios': Servicio.objects.all()
    })

@login_required
def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    visita.delete()
    return redirect('visitas')
