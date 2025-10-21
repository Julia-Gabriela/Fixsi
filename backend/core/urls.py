from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),           
    path('', views.home_view, name='home'),    
    path('login/', include('login.urls')),  
    path('sobre/', views.sobre_view, name='sobre_nos'),     
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
