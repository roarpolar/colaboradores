from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autentication.urls')),  # Use '' para a rota principal
    # from .api import api
]
