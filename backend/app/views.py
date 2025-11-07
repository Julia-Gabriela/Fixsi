from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User 
# Importa todos os modelos (incluindo os "não gerenciados")
from .models import Perfil, Profissional, Cliente, Servico, Agendamento 
from django.db.models import Q 
from datetime import date
from django.utils import timezone

# --- Views de Páginas Estáticas ---

def get_user_perfil(request):
    """Função helper para buscar o perfil do usuário logado."""
    perfil = None
    if request.user.is_authenticated:
        try:
            perfil = get_object_or_404(Perfil, user=request.user)
        except:
            perfil = None # Usuário logado mas sem perfil
    return perfil

def home_view(request):
    context = {
        'perfil': get_user_perfil(request)
    }
    return render(request, 'home.html', context)

def entrar_view(request):
    # Esta view não está sendo usada pelas suas URLs
    return render(request, 'login.html')

def sobre_view(request):
    context = {
        'perfil': get_user_perfil(request)
    }
    return render(request, 'sobre.html', context) 

def como_funciona_view(request):
    context = {
        'perfil': get_user_perfil(request)
    }
    return render(request, 'como_funciona.html', context) 

# --- View de Serviços (Busca) ---

def servicos_view(request):
    perfil = get_user_perfil(request)
    query = request.GET.get('q', None)
    context = {
        'perfil': perfil,
        'query': query
    }

    if query:
        # Normaliza a query para minúsculas para a verificação
        query_lower = query.lower()

        # 👇 INÍCIO DA NOVA LÓGICA ESTÁTICA 👇
        if query_lower == 'marceneiro':
            # Renderiza o template estático de marcenaria
            return render(request, 'static_search_marceneiro.html', context)
        
        elif query_lower == 'makita':
            # Renderiza o template estático de ferramentas
            return render(request, 'static_search_makita.html', context)
        # 👆 FIM DA NOVA LÓGICA ESTÁTICA 👆

        else:
            # Lógica original de busca no banco de dados para qualquer outra pesquisa
            servicos = Servico.objects.filter(
                Q(titulo__icontains=query) |
                Q(descricao__icontains=query) |
                Q(categoria__icontains=query)
            )
            context['servicos'] = servicos
            return render(request, 'search_results.html', context)
    
    else:
        # Se não houver query, mostra a página de categorias (servicos.html)
        return render(request, 'servicos.html', context)

# --- Views do Dashboard ---

@login_required(login_url='login') 
def dashboard_view(request):
    try:
        perfil = get_object_or_404(Perfil, user=request.user)
    except:
        perfil = None 
    context = {
        'perfil': perfil
    }
    return render(request, 'dashboard.html', context) 

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login') 
def novo_servico_view(request):
    
    # Busca o perfil logado
    perfil = get_user_perfil(request)
    if not perfil:
        messages.error(request, 'Perfil de usuário não encontrado.')
        return redirect('dashboard')

    if request.method == 'POST':
        try:
            # CORREÇÃO: O 'prestador' do Serviço é um 'Profissional', 
            # que é linkado ao 'Perfil'.
            profissional = get_object_or_404(Profissional, perfil=perfil)
        except Profissional.DoesNotExist:
            messages.error(request, 'Apenas perfis de "Profissional" podem cadastrar serviços.')
            return redirect('dashboard')

        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        preco_str = request.POST.get('preco')
        
        # CORREÇÃO: O campo 'foto' (db_column='imagem') é um CharField(255).
        # Ele espera uma URL (texto), não um upload de arquivo.
        # Assumindo que o input 'fotos' no HTML seja um <input type="text">
        foto_url = request.POST.get('fotos') 

        preco = None
        if preco_str:
            try:
                preco = float(preco_str.replace(',', '.'))
            except ValueError:
                preco = None # Salva sem preço se for inválido

        try:
            Servico.objects.create(
                prestador=profissional, # USA O OBJETO PROFISSIONAL
                titulo=titulo,
                descricao=descricao,
                categoria=categoria,
                preco=preco,
                foto=foto_url # SALVA A URL DA IMAGEM
            )
            messages.success(request, 'Novo serviço cadastrado com sucesso!')
            return redirect('dashboard') 
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao salvar o serviço: {e}')
            return redirect('novo_servico')
    
    context = {
        'perfil': perfil
    }
    return render(request, 'novo_servico.html', context)

@login_required(login_url='login')
def mensagens_view(request):
    # View atualizada para renderizar a página completa
    context = {
        'perfil': get_user_perfil(request) 
    }
    return render(request, 'mensagens_pagina.html', context)

@login_required(login_url='login')
def avaliacoes_view(request):
    context = {
        'perfil': get_user_perfil(request)
    }
    return render(request, 'avaliacoes.html', context)

@login_required(login_url='login')
def agendamentos_view(request):
    context = {
        'perfil': get_user_perfil(request)
    }
    return render(request, 'agendamentos.html', context)

@login_required(login_url='login')
def historico_view(request):
    context = { 
        'perfil': get_user_perfil(request) 
    }
    return render(request, 'historico.html', context)

# --- Views de Perfil ---

@login_required(login_url='login')
def perfil_profissional_view(request):
    # View para o perfil PÚBLICO do PRÓPRIO utilizador logado
    try:
        perfil = get_object_or_404(Perfil, user=request.user)
    except:
        perfil = None 
    context = {
        'perfil': perfil
    }
    return render(request, 'perfil_profissional.html', context) 

@login_required(login_url='login')
def perfil_cliente_view(request, user_id):
    # View para o perfil de OUTRO utilizador (cliente)
    perfil_logado = get_user_perfil(request)
    
    try:
        # 1. Encontra o utilizador cliente pelo ID da URL
        cliente_user = get_object_or_404(User, id=user_id)
        # 2. Encontra o perfil associado a esse utilizador
        # (O template 'perfil_cliente.html' usa 'cliente_perfil.imagem', 
        # então passamos o objeto Perfil)
        cliente_perfil = get_object_or_404(Perfil, user=cliente_user)
    except:
        messages.error(request, 'Perfil de cliente não encontrado.')
        return redirect('dashboard')

    context = {
        'perfil': perfil_logado, # Para o navbar
        'cliente_user': cliente_user,
        'cliente_perfil': cliente_perfil # Passa o objeto Perfil do cliente
    }
    return render(request, 'perfil_cliente.html', context) 

@login_required(login_url='login')
def editar_perfil_profissional_view(request):
    # View para EDITAR o perfil do PRÓPRIO utilizador logado
    try:
        perfil = get_object_or_404(Perfil, user=request.user)
    except:
        messages.error(request, 'Perfil não encontrado.')
        return redirect('dashboard')

    if request.method == 'POST':
        try:
            # CORREÇÃO: A 'bio' é salva na tabela 'profissional'
            profissional = Profissional.objects.get(perfil=perfil)
            profissional.bio = request.POST.get('sobre') 
            profissional.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
        except Profissional.DoesNotExist:
            messages.error(request, 'Perfil profissional não encontrado para salvar a bio.')
        
        return redirect('perfil_profissional')

    # Lógica GET (apenas mostrar a página de edição)
    context = {
        'perfil': perfil
    }
    return render(request, 'editar_perfil_profissional.html', context)

def servico_modal_view(request, service_type):
    """
    Renderiza a página de 'detalhes' (servico_modal.html)
    para diferentes tipos de serviços de marcenaria.
    """
    perfil = get_user_perfil(request)

    # Dicionário para exibir o nome legível do serviço
    service_type_display_map = {
        'moveis_planejados': 'Móveis Planejados',
        'restauracao': 'Restauração de Móveis',
        'pequenos_reparos': 'Pequenos Reparos',
        'montagem': 'Montagem de Móveis',
        'rusticos': 'Móveis Rústicos e Artesanais',
    }

    service_type_display = service_type_display_map.get(service_type, 'Serviço')

    context = {
        'perfil': perfil,
        'service_type_display': service_type_display,
        'service_type': service_type,
    }

    return render(request, 'servico_modal.html', context)

def ferramenta_modal_view(request, tool_type):
    """
    Renderiza a página de detalhes de ferramentas (ferramenta_modal.html)
    com formulário de aluguel.
    """
    perfil = get_user_perfil(request)

    tool_map = {
        'martelete': {
            'nome': 'Martelete Perfurador 2kg',
            'descricao': 'Ideal para perfuração em concreto e pequenas demolições.',
            'valor': 'R$ 80,00 / dia'
        },
        'parafusadeira': {
            'nome': 'Parafusadeira a Bateria 12V',
            'descricao': 'Compacta, leve e com impacto. Ideal para montagem de móveis.',
            'valor': 'R$ 50,00 / dia'
        },
        'serra_circular': {
            'nome': 'Serra Circular 7 1/4"',
            'descricao': 'Cortes precisos em madeira com ajuste de profundidade.',
            'valor': 'R$ 65,00 / dia'
        },
        'lixadeira': {
            'nome': 'Lixadeira Orbital',
            'descricao': 'Perfeita para acabamento em madeira e massa corrida.',
            'valor': 'R$ 45,00 / dia'
        },
        'tupia': {
            'nome': 'Tupia de Coluna',
            'descricao': 'Para entalhes e acabamentos profissionais em madeira.',
            'valor': 'R$ 70,00 / dia'
        },
    }

    tool = tool_map.get(tool_type, {
        'nome': 'Ferramenta Desconhecida',
        'descricao': 'Informações não disponíveis.',
        'valor': 'R$ --'
    })

    # Caso o formulário seja enviado
    if request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente')
        data_retirada = request.POST.get('data_retirada')
        data_devolucao = request.POST.get('data_devolucao')

        # Validação simples
        if not nome_cliente or not data_retirada or not data_devolucao:
            messages.error(request, 'Preencha todos os campos do formulário.')
        else:
            messages.success(request, f'Aluguel de {tool["nome"]} reservado com sucesso!')
            return redirect('servicos')  # volta à página de serviços

    context = {
        'perfil': perfil,
        'tool': tool,
        'hoje': date.today().isoformat()
    }

    return render(request, 'ferramenta_modal.html', context)
