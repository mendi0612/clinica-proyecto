from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path('crear_cita/', views.crear_cita),
    path('gestion/', views.gestion_citas),
    path('mis_citas/', views.mis_citas),
    path('eliminar_cita/<int:id>/', views.eliminar_cita),
    path('editar_cita/<int:id>/', views.editar_cita),
]