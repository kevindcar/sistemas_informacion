from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import  login, authenticate
from .models import Vehiculo
from .forms import UsuarioForm

def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vehiculos')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {
        'form': form
    })

def home_view(request):
    return render(request, 'home.html')

def sala_espera_view(request):
    return render(request, 'sala_espera.html')

def vehiculos_view(request):
    vehiculos = Vehiculo.objects.filter(disponible=True)
    return render(request, 'vehiculos.html', {'vehiculos': vehiculos})
def sala_espera(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.user = request.user
            usuario.save()
            return redirect('vehiculos_disponibles')
    else:
        form = UsuarioForm()
    return render(request, 'sala_espera.html', {'form': form})
    

def vehiculos_disponibles(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos.html', {'vehiculos': vehiculos})