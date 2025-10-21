from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

def entrar_view(request):
    return render(request, 'login.html')

def sobre_view(request):
    return render(request, 'sobre.html')


