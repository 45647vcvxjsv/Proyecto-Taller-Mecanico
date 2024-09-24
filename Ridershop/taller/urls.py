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
from app1.views import indexview, crear_cita, cita_confirmacion
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexview, name='index'),
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.perfil_cliente, name='perfil_cliente'),
    path('crear-cita/', crear_cita, name='crear_cita'),
    path('confirmacion-cita/<int:cita_id>/', cita_confirmacion, name='cita_confirmacion'),
]
