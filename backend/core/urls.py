# /backend/core/urls.py

from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

# Apenas UMA lista urlpatterns com todas as rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('sobre/', views.sobre_nos, name="sobre_nos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])