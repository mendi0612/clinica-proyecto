from django.shortcuts import render, get_object_or_404
from .models import Paciente, HistoriaClinica


def inicio(request):
    # Se consultan todos los pacientes desde la base de datos
    pacientes = Paciente.objects.all()

    return render(request, 'index.html', {
        'pacientes': pacientes
    })


def historia_clinica(request, paciente_id):
    # Se busca el paciente por su ID, si no existe devuelve 404
    paciente = get_object_or_404(Paciente, id=paciente_id)

    # Se obtienen todas las historias clinicas del paciente
    historias = paciente.historias.all().order_by('-fecha_creacion')

    return render(request, 'historia_clinica.html', {
        'paciente': paciente,
        'historias': historias
    })
