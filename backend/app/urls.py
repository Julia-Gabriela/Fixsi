from django.urls import path
from . import views
from django.contrib.auth.models import User # Necessário para a view de cliente

# A sua lista de urlpatterns começa aqui
urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre_nos'),
    path('como-funciona/', views.como_funciona_view, name='como_funciona'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('sair/', views.logout_view, name='logout'),
    path('servico/novo/', views.novo_servico_view, name='novo_servico'),
    
    # Rotas que adicionámos para o dashboard
    path('mensagens/', views.mensagens_view, name='mensagens'),
    path('avaliacoes/', views.avaliacoes_view, name='avaliacoes'),
    path('agendamentos/', views.agendamentos_view, name='agendamentos'),
    path('historico/', views.historico_view, name='historico'),
    
    # Rotas de perfil (do plano anterior)
    path('perfil/profissional/', views.perfil_profissional_view, name='perfil_profissional'),
    
    # 👇 NOVA ROTA ADICIONADA AQUI 👇
    path('perfil/profissional/editar/', views.editar_perfil_profissional_view, name='editar_perfil_profissional'),
    
    path('perfil/cliente/<int:user_id>/', views.perfil_cliente_view, name='perfil_cliente'),

    path('servico/<str:service_type>/', views.servico_modal_view, name='servico_modal'),

    # Rota para exibir o modal de ferramentas (detalhes)
path('ferramenta/<str:tool_type>/', views.ferramenta_modal_view, name='ferramenta_modal'),

]