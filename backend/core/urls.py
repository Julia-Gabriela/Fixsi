from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),        
    
    # 2. Inclui as URLs do app 'login' (ex: /login/)
    path('login/', include('login.urls')),  
    path('', include('app.urls')), 

    # 4. As linhas abaixo foram REMOVIDAS daqui,
    # pois elas agora vivem dentro de 'app.urls.py'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)