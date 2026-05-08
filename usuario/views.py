from django.shortcuts import render
from django.http import HttpResponse

def usuario(request):
    return render(request, "Login.html") 

def Registro(request):
    return render(request, "Registro.html")

def MenuPrincipal(request):
    return render(request, "MenuInicio.html")

def inicio(request):
    return render(request, 'inicio.html')
