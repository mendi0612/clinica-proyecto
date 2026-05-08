from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path("Login/", views.usuario),
    path("Registro/", views.Registro),
    path("MenuPrincipal/", views.MenuPrincipal),
    path('inicio/', views.inicio)
]