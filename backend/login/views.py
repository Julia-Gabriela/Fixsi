from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('area_cliente')  
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  



@login_required(login_url='login')
def area_cliente_view(request):
    return render(request, 'login/area_cliente.html')
