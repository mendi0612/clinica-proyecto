from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('medicamentos/', views.lista_medicamentos),
    path('dispensaciones/',views.lista_dispensaciones),
    path('tickets/', views.lista_tickets),
    path('sedes/', views.lista_sedes)
]
