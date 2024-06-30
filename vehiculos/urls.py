
from django.urls import path
from .views import login_view, home_view, sala_espera_view, vehiculos_view, sala_espera, vehiculos_disponibles


urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('sala_espera/', sala_espera, name='sala_espera'),
    path('sala_espera/', sala_espera_view, name='sala_espera'),
    path('vehiculos/', vehiculos_view, name='vehiculos'),
    path('vehiculos_disponibles/', vehiculos_disponibles, name='vehiculos_disponibles'),
    # otras rutas...
]
