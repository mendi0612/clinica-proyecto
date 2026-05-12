from django.shortcuts import render
from django.http import HttpResponse
from .models import Cita



def gestion_citas(request):
    return render(request, "Gestion_citas.html")

def asignacion(request):
    return render(request, "Modulo.html")


def consulta(request):

    citas = Cita.objects.all()
    print(citas.values())

    return render(request, "Consulta.html", {
        
        "citas": citas
    })

def modificacion(request):
    return render(request, "Modificacion.html")

def cancelacion(request):
    return render(request, "Cancelacion.html")


