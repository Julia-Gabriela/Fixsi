from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import login_required
from .models import Perfil

def home_view(request):
    return render(request, 'home.html')

def entrar_view(request):
    return render(request, 'login.html')

def sobre_view(request):
    return render(request, 'sobre.html')

def como_funciona_view(request):
    return render(request, 'como_funciona.html')

def servicos_view(request):
    return render(request, 'servicos.html')

@login_required 
def dashboard_view(request):
    try:
        perfil = get_object_or_404(Perfil, user=request.user)
    except:
        perfil = None 

    context = {
        'perfil': perfil
    }
    return render(request, 'dashboard.html', context)