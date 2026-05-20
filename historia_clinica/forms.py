from django import forms
from .models import Paciente, HistoriaClinica


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'documento', 'fecha_nacimiento', 'telefono', 'direccion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['motivo_consulta', 'diagnostico', 'tratamiento', 'observaciones']
