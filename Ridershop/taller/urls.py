"""
URL configuration for taller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import indexview, crear_cita, cita_confirmacion, registro_usuario, perfil_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexview, name='index'),  # Página de inicio
    path('registro/', registro_usuario, name='registro'),  # Registro de usuario
    path('perfil/', perfil_cliente, name='perfil_cliente'),  # Perfil del cliente
    path('crear-cita/', crear_cita, name='crear_cita'),  # Crear cita
    path('cita-confirmacion/<int:cita_id>/', cita_confirmacion, name='cita_confirmacion'),  # Confirmación de cita
]
