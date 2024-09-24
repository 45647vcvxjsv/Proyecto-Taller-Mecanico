from django import forms
from app1.models import Cita, PerfilClientes

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['usuario','vehiculo', 'mecanico', 'fecha', 'hora', 'tipo_servicio']

class PerfilClienteForm(forms.ModelForm):
    class Meta:
        model = PerfilClientes
        fields = ['usuario','telefono', 'email']