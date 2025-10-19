from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def sobre_view(request):
    return render(request, 'sobre.html')
