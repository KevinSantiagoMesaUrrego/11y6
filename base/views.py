from django.shortcuts import redirect, render

from usuario.forms import PersonalizarForm, PersonalizarUpdateForm
from usuario.models import  Eps, Turno, Trabajador
from venta.models import Venta,Detalle_venta, Reserva, Ubicacion
from compra.models import Compra, Detalle_compra, Evento, Proveedor, Personalizacion
from inventario.models import Presentacion, Marca, ConsumoTrabajador, Producto, UnidadMedida
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from compra.models import Personalizacion
@login_required
def principal(request):

    titulo="Bienvenido al Sistema de william"
    personalizar=Personalizacion.objects.all()
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
        "titulo":titulo,
        "personalizar":personalizar
    }
    return render(request, "index.html", context)

def logout_user(request):
    logout(request)
    return redirect('inicio')
def ayuda(request):
    return render(request, "partials/ayuda.html")
def personalizar_modificar(request,pk):
    titulo="Personalizar"
    personalizar= Personalizacion.objects.get(id=pk)
    if request.method== 'POST':
        form= PersonalizarUpdateForm(request.POST, instance=personalizar)
        if form.is_valid():
            form.save()
            messages.success(request, 'La imagen se modifico correctamente.')
            return redirect('personalizar')
    else:
        form= PersonalizarUpdateForm(instance=personalizar)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "personalizar.html",context)

def personalizar_eliminar(request, pk):
    Personalizacion.objects.filter(id=pk).delete()
    messages.success(request,'La imagen se eliminó correctamente.')
    return redirect('personalizar')
def personalizar(request):
    titulo="Personalizar"
    modulo = "base"
    personalizar=Personalizacion.objects.all()
    if request.method== 'POST':
        form= PersonalizarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agregó la imagen correctamente.')
            return redirect('personalizar')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= PersonalizarForm()
    context={
        "titulo":titulo,
        "form":form,
        "modulo":modulo,
        "personalizar":personalizar,
    }
    return render(request, "partials/personalizar.html",context)


