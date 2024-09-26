from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from app1.models import Cita
from app1.forms import CitaForm 
from .models import PerfilCliente
from .forms import PerfilClienteForm

# Vista para la página principal
def indexview(request):
    return render(request, 'index.html')

# Vista para crear una cita
@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user  
            cita.save()
            return redirect('cita_confirmacion', cita_id=cita.id)  # Redirigir a la vista de confirmación de la cita
    else:
        initial_data = {
            'nombre': request.user.get_full_name(),  # Suponiendo que estás usando first_name y last_name
            'email': request.user.email,
            'telefono': request.user.perfilcliente.telefono if hasattr(request.user, 'perfilcliente') else ''
        }
        form = CitaForm(initial=initial_data)
    return render(request, 'crear_cita.html', {'form': form})

# Vista para la confirmación de la cita
@login_required
def cita_confirmacion(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'cita_confirmacion.html', {'cita': cita})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)  
            return redirect('perfil_cliente')  # Redirigir a la vista de perfil del cliente
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


# Vista para la gestión del perfil del cliente
@login_required
def perfil_cliente(request):
    perfil, created = PerfilCliente.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilClienteForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('crear_cita')  # Redirigir a la vista de crear cita después de guardar el perfil
    else:
        form = PerfilClienteForm(instance=perfil)
    
    return render(request, 'perfil_cliente.html', {'form': form})
