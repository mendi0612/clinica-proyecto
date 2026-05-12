from django.db import models

class Cita(models.Model):

    nombre_medico = models.CharField(max_length=100)

    horario_disponible = models.TimeField()

    fecha_disponible = models.DateField()

    sede_disponible = models.CharField(max_length=100)

    especialidad = models.CharField(max_length=100)

    estado = models.CharField(
        max_length=50,
        default="Disponible"
    )

    def __str__(self):
        return f"{self.nombre_medico} - {self.fecha_disponible}"