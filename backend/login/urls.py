from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Etapa 1 do cadastro
    path('cadastro/', views.cadastro1, name='cadastro1'),

    # Etapa 2 do cadastro
    path('cadastro/passo2/', views.cadastro2, name='cadastro2'),

    # Página logada
    path('area_logada/', views.area_logada_view, name='area_logada'),

    # Tela 1: "Redefinir senha" (Pede o email)
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), 
         name="password_reset"),

    # Tela 2: "Pop email enviado" (Aviso de sucesso)
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
         name="password_reset_done"),

    # Tela 3: "Redefinindo senha" (O link que vai no email)
    # <uidb64> e <token> são gerados automaticamente pelo Django
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
         name="password_reset_confirm"),

    # Tela 4: "senha redefinida" (Sucesso final)
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),

]
