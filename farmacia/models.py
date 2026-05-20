from django.db import models
from django.utils import timezone


# =========================
# CATEGORIAS
# =========================
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# =========================
# PRODUCTOS
# =========================
class Producto(models.Model):

    ESTADOS = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )

    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos'
    )

    descripcion = models.TextField(blank=True, null=True)

    codigo_barras = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    precio_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    stock_minimo = models.PositiveIntegerField(default=5)

    fecha_vencimiento = models.DateField(blank=True, null=True)

    laboratorio = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='ACTIVO'
    )

    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - Stock: {self.stock}"


# =========================
# FACTURA
# =========================
class Factura(models.Model):

    METODOS_PAGO = (
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('NEQUI', 'Nequi'),
        ('DAVIPLATA', 'Daviplata'),
    )

    numero_factura = models.CharField(
        max_length=20,
        unique=True
    )

    cliente = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    fecha = models.DateTimeField(default=timezone.now)

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    iva = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS_PAGO,
        default='EFECTIVO'
    )

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Factura {self.numero_factura}"


# =========================
# DETALLE FACTURA
# =========================
class DetalleFactura(models.Model):

    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        related_name='detalles'
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.PositiveIntegerField()

    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"