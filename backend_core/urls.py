from django.contrib import admin
from django.urls import path
from .api import api  # Importa a API principal


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),  # Certifique-se de que essa linha está mapeando corretamente
]
