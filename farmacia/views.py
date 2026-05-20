import json
import random

from decimal import Decimal

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Producto,
    Categoria,
    Factura,
    DetalleFactura
)


# =========================
# FARMACIA
# =========================

def farmacia(request):

    productos = Producto.objects.filter(
        estado='ACTIVO'
    )

    categorias = Categoria.objects.all()

    contexto = {

        'productos': productos,
        'categorias': categorias
    }

    return render(
        request,
        'farmacia.html',
        contexto
    )


# =========================
# CARRITO
# =========================

def carrito(request):

    return render(
        request,
        'carrito.html'
    )


# =========================
# FACTURACION
# =========================

def facturacion(request):

    return render(
        request,
        'facturacion.html'
    )


# =========================
# FINALIZAR FACTURA
# =========================

@csrf_exempt
def finalizar_factura(request):

    if request.method == 'POST':

        data = json.loads(
            request.body
        )

        carrito = data.get(
            'carrito',
            []
        )

        subtotal = Decimal('0')


        # =========================
        # CREAR FACTURA
        # =========================

        numero = random.randint(
            10000,
            99999
        )

        factura = Factura.objects.create(

            numero_factura=f"FAC-{numero}",

            subtotal=0,

            iva=0,

            total=0,

            metodo_pago='EFECTIVO'
        )


        # =========================
        # RECORRER CARRITO
        # =========================

        for item in carrito:
            producto = Producto.objects.get(
                id=item['id']
            )

            cantidad = int(
                item['cantidad']
            )

            precio = Decimal(

                str(item['precio'])
                .replace("$", "")
                .replace(".", "")
                .replace(",", "")

            )

            sub = precio * cantidad

            subtotal += sub


            # =========================
            # DETALLE FACTURA
            # =========================

            DetalleFactura.objects.create(

                factura=factura,

                producto=producto,

                cantidad=cantidad,

                precio_unitario=precio,

                subtotal=sub
            )


            # =========================
            # DESCONTAR STOCK
            # =========================

            producto.stock -= cantidad

            producto.save()


        # =========================
        # CALCULOS
        # =========================

        iva = subtotal * Decimal('0.19')

        total = subtotal + iva


        factura.subtotal = subtotal

        factura.iva = iva

        factura.total = total

        factura.save()


        return JsonResponse({

            'success': True,

            'factura': factura.numero_factura
        })


    return JsonResponse({

        'success': False
    })