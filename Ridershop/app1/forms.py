from django import forms
from app1.models import Cita, PerfilCliente

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['vehiculo', 'mecanico', 'fecha', 'hora', 'tipo_servicio', 'comentarios']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if self.usuario:
            self.fields['vehiculo'].queryset = self.usuario.vehiculo_set.all()  

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefono'].label = 'Número de Teléfono'
        self.fields['telefono'].widget.attrs.update({
            'placeholder': 'Ingresa tu número de teléfono',
            'class': 'form-control'  # Agregar clase de Bootstrap para estilos
        })

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit() or len(telefono) < 7:
            raise forms.ValidationError("Por favor, ingresa un número de teléfono válido.")
        return telefono
