from django.shortcuts import redirect, render
from usuario.models import Persona, Eps, Turno, Trabajador
from venta.models import Venta,Detalle_venta, Reserva, Ubicacion
from compra.models import Compra, Detalle_compra, Evento, Proveedor
from inventario.models import Presentacion, Marca, ConsumoTrabajador, Producto, UnidadMedida
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def principal(request):

    titulo="Bienvenido al Sistema de william"
    persona=Persona.objects.all().count()
    eps=Eps.objects.all().count()
    turno=Turno.objects.all().count()
    trabajador=Trabajador.objects.all().count()
    venta=Venta.objects.all().count()
    detalle_venta=Detalle_venta.objects.all().count()
    reserva=Reserva.objects.all().count()
    ubicacion=Ubicacion.objects.all().count()
    compra=Compra.objects.all().count()
    detalle_compra=Detalle_compra.objects.all().count()
    evento=Evento.objects.all().count()
    proveedor=Proveedor.objects.all().count()
    presentacion=Presentacion.objects.all().count()
    marca=Marca.objects.all().count()
    consumo_trabajador=ConsumoTrabajador.objects.all().count()
    producto=Producto.objects.all().count()
    unidad_medida=UnidadMedida.objects.all().count()
    context={
        "personas": persona,
        "eps": eps,
        "turnos": turno,
        "trabajadores": trabajador,
        "ventas": venta,
        "detalle_ventas": detalle_venta,
        "reservas": reserva,
        "ubicaciones": ubicacion,
        "compras": compra,
        "detalle_compras": detalle_compra,
        "eventos": evento,
        "proveedores": proveedor,
        "productos": producto,
        "presentaciones": presentacion,
        "marcas": marca,
        "unidad_medidas": unidad_medida,
        "consumo_trabajadores": consumo_trabajador,
        "titulo":titulo
    }
    return render(request, "index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')
