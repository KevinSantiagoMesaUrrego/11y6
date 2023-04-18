from django.urls import path
from venta.views import venta_crear,venta_listar,venta_modificar,venta_eliminar
from venta.views import detalle_venta_crear,detalle_venta_listar,detalle_venta_modificar,detalle_venta_eliminar
from venta.views import reserva_crear,reserva_listar,reserva_modificar,reserva_eliminar
from venta.views import ubicacion_crear,ubicacion_listar,ubicacion_modificar,ubicacion_eliminar

urlpatterns = [
    path('venta/', venta_listar, name="venta" ),
    path('venta_crear/', venta_crear, name="venta-crear"),
    path('venta_modificar/<int:pk>/', venta_modificar, name="venta-modificar"),
    path('venta_eliminar/<int:pk>/', venta_eliminar, name="venta-eliminar"),
    path('detalle_venta/', detalle_venta_listar, name="detalle_venta"),
    path('detalle_venta_crear/', detalle_venta_crear, name="detalle_venta-crear"),
    path('detalle_venta_modificar/<int:pk>/', detalle_venta_modificar, name="detalle_venta-modificar"),
    path('detalle_venta_eliminar/<int:pk>/', detalle_venta_eliminar, name="detalle_venta-eliminar"),
    path('reserva/',reserva_listar,name="reserva"),
    path('reserva_crear/',reserva_crear,name="reserva-crear"),
    path('reserva_modiifcar/<int:pk>/',reserva_modificar,name="reserva-modificar"),
    path('reserva_eliminar/<int:pk>/',reserva_eliminar,name="reserva-eliminar"),
    path('ubicacion/',ubicacion_listar,name="ubicacion"),
    path('ubicacion_crear/',ubicacion_crear,name="ubicacion-crear"),
    path('ubicacion_modificar/<int:pk>/',ubicacion_modificar,name="ubicacion-modificar"),
    path('ubicacion_eliminar/<int:pk>/',ubicacion_eliminar,name="ubicacion-eliminar"),
]