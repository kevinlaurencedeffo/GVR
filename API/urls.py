
from django.contrib import admin
from API import settings
from django.conf.urls.static import static
from django.urls import path, include
from comptes.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('stocks/', include('stocks.urls')),
    path('personnel/', include('personnels.urls')),
    path('caisse/', include('caisse.urls')),
    path('',include('comptes.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 
   