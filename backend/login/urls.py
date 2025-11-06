from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Etapa 1 do cadastro
    path('cadastro/', views.cadastro1, name='cadastro1'),

    # Etapa 2 do cadastro
    path('cadastro/passo2/', views.cadastro2, name='cadastro2'),

    # Página logada
    path('area_logada/', views.area_logada_view, name='area_logada'),

]
