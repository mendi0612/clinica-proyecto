from django.shortcuts import render, get_object_or_404

from farmacia.models import Factura, DetalleFactura


def lista_facturas(request):

    facturas = Factura.objects.all().order_by('-fecha')

    return render(
        request,
        'lista_facturas.html',
        {
            'facturas': facturas
        }
    )


def detalle_factura(request, id):

    factura = get_object_or_404(
        Factura,
        id=id
    )

    detalles = DetalleFactura.objects.filter(
        factura=factura
    )

    return render(
        request,
        'detalle_factura.html',
        {
            'factura': factura,
            'detalles': detalles
        }
    )