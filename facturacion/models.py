from django.db import models


class Factura(models.Model):

    numero = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Factura {self.numero}"