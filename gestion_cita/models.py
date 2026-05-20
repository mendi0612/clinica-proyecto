from django.db import models
from usuario.models import Usuario


# =========================
# ESPECIALIDADES
# =========================
class Especialidad(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre


# =========================
# DOCTORES
# =========================
class Doctor(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE
    )

    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE
    )

    telefono = models.CharField(max_length=20)

    consultorio = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):

        return f"Dr. {self.nombre}"
# =========================
# CITAS
# =========================
class Cita(models.Model):

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
        ('Finalizada', 'Finalizada'),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    hora = models.TimeField()

    motivo = models.TextField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Pendiente'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )
    