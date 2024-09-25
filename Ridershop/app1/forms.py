from django import forms
from app1.models import Cita, PerfilCliente

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['vehiculo', 'mecanico', 'fecha', 'hora', 'tipo_servicio', 'comentarios']

    # Si quieres que el usuario autenticado se asigne automáticamente en lugar de pedirlo en el formulario:
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if self.usuario:
            self.fields['vehiculo'].queryset = self.usuario.vehiculo_set.all()  # Filtrar vehículos del usuario

    def save(self, commit=True):
        cita = super().save(commit=False)
        if self.usuario:
            cita.usuario = self.usuario  
        if commit:
            cita.save()
        return cita

class PerfilClienteForm(forms.ModelForm):
    class Meta:
        model = PerfilCliente
        fields = ['telefono']

    # Si deseas evitar que el campo 'usuario' sea visible o modificable en el formulario de perfil:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefono'].label = 'Número de Teléfono'
