from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre_nos'),
    path('como-funciona/', views.como_funciona_view, name='como_funciona'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

