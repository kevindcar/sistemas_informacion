from django import forms
from django.contrib.auth.models import User
from .models import Reserva
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['vehiculo']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'numero_identidad', 'vehiculo_preferencia']

