from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path("gestion/", views.gestion_citas),
    path("asignacion/", views.asignacion),
    path("consulta/", views.consulta),
    path("modificacion/", views.modificacion),
    path("cancelacion/", views.cancelacion)
]