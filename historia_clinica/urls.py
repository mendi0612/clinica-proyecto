from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('historia/<int:paciente_id>/', views.historia_clinica, name='historia_clinica'),
]
