from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length= 50)
    fecha_vencimiento = models.DateField()
    precio = models.DecimalField (max_digits = 10, decimal_places= 2, default = 0)
    requiere_formula = models.BooleanField (default=False)
    stock = models.IntegerField(default= 0)

    def __str__(self):
        return f"Medicamento: {self.nombre}"

class Dispensacion(models.Model):
    medicamento = models.CharField(max_length= 30)
    paciente = models.CharField (max_length =90)
    cantidad = models.IntegerField()
    fecha_entrega = models.DateField(auto_now_add=True)
    indicaciones_medicas = models.TextField(blank=True)

    def __str__(self):
        return f"Dispensacion: {self.medicamento}"
        return f"Dispensacion: {self.paciente}"