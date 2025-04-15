
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #rota padrão do admin do Django
    path('api/', include('api_rest.urls')), # arquivo com os enpoints de API
    path('pages/', include('api_rest.urls_html')) # arquivo com os endpoints de front
]
