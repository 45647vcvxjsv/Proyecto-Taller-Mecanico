from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from app1.models import Cita
from app1.forms import CitaForm 
from .models import PerfilClientes
from .forms import PerfilClienteForm

def indexview(request):
    return render(request, 'index.html')

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_confirmacion', cita_id=Cita.id)  # Redirige a una página de éxito o al índice
    else:
        form = CitaForm()
    return render(request, 'crear_cita.html', {'form': form})

def cita_confirmacion(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'cita_confirmacion.html', {'cita': cita})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Perfil_Cliente')  # Redirige a la página de perfil del cliente
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})



@login_required
def perfil_cliente(request):
    try:
        perfil = request.user.perfilcliente
    except PerfilClientes.DoesNotExist:
        perfil = PerfilClientes(usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilClienteForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('crear_cita')
    else:
        form = PerfilClienteForm(instance=perfil)
    
    return render(request, 'perfil_cliente.html', {'form': form})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.cliente = request.user
            cita.save()
            return redirect('cita_confirmacion', cita_id=cita.id)
    else:
        initial_data = {
            'nombre': request.user.get_full_name(),
            'email': request.user.email,
            'telefono': request.user.perfilcliente.telefono if hasattr(request.user, 'perfilcliente') else ''
        }
        form = CitaForm(initial=initial_data)
    return render(request, 'crear_cita.html', {'form': form})






