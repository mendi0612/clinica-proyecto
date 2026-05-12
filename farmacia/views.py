from django.shortcuts import render
from django.http import HttpResponse
from .models import Medicamento, Dispensacion, Ticket, Sede

def home(request):
    data = {
        'nombre_usuario': 'Paula'
    }
    return render(request, 'home.html', data)

def lista_medicamentos(request):
    data = {
        'medicamentos': Medicamento.objects.all()
    }
    return render(request, 'lista_medicamentos.html', data) 

def lista_dispensaciones(request):
    data = {
        'dispensaciones': Dispensacion.objects.all()
    }
    return render(request, 'lista_dispensaciones.html', data)

def lista_tickets(request): 
    data = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'lista_tickets.html', data)

def lista_sedes(request):
    data = {
        'sedes': Sede.objects.all()
    }
    return render(request, 'lista_sedes.html', data)
