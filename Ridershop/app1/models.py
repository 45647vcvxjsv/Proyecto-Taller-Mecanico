
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('reparado', 'Reparado'),
        ('no_reparado', 'No reparado'),
    ]
    
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    fecha_ultima_reparacion = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='no_reparado',
    )

class Mecánico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    

class Reparacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=100)
    descripcion = models.TextField()

class Cita(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecánico, on_delete=models.CASCADE, default=1)
    mecanico = models.ForeignKey(Mecánico, null=True, blank=True, on_delete=models.SET_NULL)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_servicio = models.CharField(max_length=100)
    comentarios = models.TextField(blank=True)
    
class PerfilClientes(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.usuario.username



