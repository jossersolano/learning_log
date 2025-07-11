"""Define patrones de URL para accounts."""
from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    # Incluye url de autenticación predeterminadas.
    path('', include('django.contrib.auth.urls')),
    # Página de registro.
    path('register/', views.register, name='register')
]