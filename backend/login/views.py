from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil, Cliente, Profissional


# ---------- LOGIN ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # <- volta a usar 'username'
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo(a), {user.first_name or user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login.html')


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('login')


# ---------- ÁREA LOGADA ----------
@login_required(login_url='login')
def area_logada_view(request):
    return render(request, 'area_logada.html')


# ---------- CADASTRO ETAPA 1 ----------
def cadastro1(request):
    if request.method == 'POST':
        dados = {
            'nome': request.POST.get('nome'),
            'email': request.POST.get('email'),
            'senha': request.POST.get('senha'),
            'confirmar_senha': request.POST.get('confirmar_senha'),
            'cpf': request.POST.get('cpf'),
            'telefone': request.POST.get('telefone'),
            'data_nascimento': request.POST.get('data_nascimento')
        }

        # Validação básica
        if dados['senha'] != dados['confirmar_senha']:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro1.html')

        request.session['dados_cadastro'] = dados
        return redirect('cadastro2')

    return render(request, 'cadastro1.html')


# ---------- CADASTRO ETAPA 2 ----------
def cadastro2(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        dados = request.session.get('dados_cadastro')

        if not dados:
            messages.warning(request, "Dados da primeira etapa não encontrados.")
            return redirect('cadastro1')

        if not tipo:
            messages.error(request, "Selecione se você é cliente ou profissional.")
            return render(request, 'cadastro2.html')

        if User.objects.filter(username=dados['email']).exists():
            messages.error(request, "E-mail já cadastrado.")
            return redirect('cadastro1')

        user = User.objects.create_user(
            username=dados['email'],
            email=dados['email'],
            password=dados['senha'],
            first_name=dados['nome']
        )

        perfil = Perfil.objects.create(
            user=user,
            cpf=dados['cpf'],
            telefone=dados['telefone'],
            data_nascimento=dados['data_nascimento'],
            tipo=tipo
        )

        if tipo == 'cliente':
            Cliente.objects.create(
                perfil=perfil,
                endereco=request.POST.get('endereco'),
                cidade=request.POST.get('cidade'),
                estado=request.POST.get('estado')
            )
        else:
            Profissional.objects.create(
                perfil=perfil,
                area_atuacao=request.POST.get('area_atuacao'),
                experiencia=request.POST.get('experiencia'),
                bio=request.POST.get('bio'),
                endereco=request.POST.get('endereco'),
                cidade=request.POST.get('cidade'),
                estado=request.POST.get('estado')
            )

        login(request, user)
        messages.success(request, f"Bem-vindo(a), {user.first_name}! Seu cadastro foi concluído com sucesso.")
        return redirect('area_logada')

    return render(request, 'cadastro2.html')