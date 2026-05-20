from django.db import models
from usuario.models import Usuario
from gestion_cita.models import Cita

# =========================
# HISTORIA CLINICA
# =========================
class HistoriaClinica(models.Model):

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE
    )

    alergias = models.TextField(
        blank=True,
        null=True
    )

    antecedentes = models.TextField(
        blank=True,
        null=True
    )

    enfermedades_cronicas = models.TextField(
        blank=True,
        null=True
    )

    grupo_sanguineo = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    observaciones_generales = models.TextField(
        blank=True,
        null=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"Historia Clínica - {self.usuario}"


# =========================
# CONSULTA MEDICA
# =========================
class ConsultaMedica(models.Model):

    cita = models.OneToOneField(
        Cita,
        on_delete=models.CASCADE
    )

    historia_clinica = models.ForeignKey(
        HistoriaClinica,
        on_delete=models.CASCADE
    )

    sintomas = models.TextField()

    diagnostico = models.TextField()

    tratamiento = models.TextField()

    receta = models.TextField(
        blank=True,
        null=True
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    fecha_consulta = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Consulta #{self.id}"


# =========================
# RESULTADO EXAMENES
# =========================
class ResultadoExamen(models.Model):

    consulta = models.ForeignKey(
        ConsultaMedica,
        on_delete=models.CASCADE
    )

    nombre_examen = models.CharField(
        max_length=200
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    resultado = models.TextField()

    archivo = models.FileField(
        upload_to='resultados_examenes/',
        blank=True,
        null=True
    )

    fecha_examen = models.DateField()

    fecha_subida = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.nombre_examen