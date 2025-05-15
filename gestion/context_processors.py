from .models import Empresa

def user_has_empresa(request):
    return {
        'user_has_empresa': request.user.is_authenticated and Empresa.objects.filter(usuario=request.user).exists()
    }

def empresa(request):
    if request.user.is_authenticated:
        empresa = Empresa.objects.filter(usuario=request.user).first()
    else:
        empresa = None
    return {
        'empresa': empresa
    }