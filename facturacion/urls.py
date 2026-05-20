from django.urls import path

from . import views


urlpatterns = [

    path('facturas/', views.lista_facturas),
    path('factura/<int:id>/', views.detalle_factura),
]