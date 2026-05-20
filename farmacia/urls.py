from django.urls import path
from . import views

urlpatterns = [
 
    path('farmacia/', views.farmacia),
    path('carrito/', views.carrito),
    path('facturacion/', views.facturacion),
    path('finalizar_factura/', views.finalizar_factura),

]   