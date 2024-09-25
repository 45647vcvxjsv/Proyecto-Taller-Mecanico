from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('reparado', 'Reparado'),
        ('no_reparado', 'No reparado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    fecha_ultima_reparacion = models.DateField(null=True, blank=True, verbose_name="Fecha última reparación")
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='no_reparado',
        verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.usuario.username}"

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        verbose_name="Teléfono"
    )
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Mecánico"
        verbose_name_plural = "Mecánicos"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reparacion(models.Model):
    ESTADO_CHOICES = [
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_proceso', verbose_name="Estado")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Reparación"
        verbose_name_plural = "Reparaciones"

    def __str__(self):
        return f"Reparación de {self.vehiculo} - {self.fecha_ingreso}"

class Cita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    mecanico = models.ForeignKey(Mecanico, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Mecánico")
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    tipo_servicio = models.CharField(max_length=100, verbose_name="Tipo de servicio")
    comentarios = models.TextField(blank=True, verbose_name="Comentarios")
    reparacion = models.OneToOneField('Reparacion', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Reparación")

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

    def __str__(self):
        return f"Cita de {self.usuario.username} - {self.fecha}"

class PerfilCliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    telefono = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        verbose_name="Teléfono"
    )

    class Meta:
        verbose_name = "Perfil de cliente"
        verbose_name_plural = "Perfiles de clientes"

    def __str__(self):
        return self.usuario.username
