from django.shortcuts import render,redirect
from venta.models import Venta,Detalle_venta,Reserva,Ubicacion
from venta.forms import VentaForm,VentaUpadteForm,Detalle_ventaForm,Detalle_ventaUpadteForm,ReservaForm,ReservaUpdateForm,UbicacionForm,UbicacionUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
#VENTA
@login_required
@permission_required("venta.add_venta", login_url="index")
def venta_crear (request):
    titulo="Venta"
    if request.method=='POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('venta')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=VentaForm()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request, "ventas/venta/crear.html", context)
@login_required
@permission_required("venta.view_venta", login_url="index")
def venta_listar(request):
    titulo="Venta"
    modulo="ventas"
    venta=Venta.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "ventas":venta
    }
    return render(request, "ventas/venta/listar.html", context)
@login_required
@permission_required("venta.change_venta", login_url="index")
def venta_modificar(request,pk):
    titulo="Venta"
    venta=Venta.objects.get(id=pk)
    if request.method== 'POST':
        form= VentaUpadteForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('venta')
    else:
        form= VentaUpadteForm(instance=venta)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "ventas/venta/modificar.html", context)
@login_required
@permission_required("venta.delete_venta", login_url="index")
def venta_eliminar(request,pk):
    venta= Venta.objects.filter(id=pk)
    venta.delete()
    venta.update(
    )
    messages.success(request,'La venta se elimino correctamente.')
    return redirect('venta')
#DETALLE VENTA
@login_required
@permission_required("venta.add_detalle_venta", login_url="index")
def detalle_venta_crear (request):
    titulo="Detalle venta"
    if request.method=='POST':
        form=Detalle_ventaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('detalle_venta')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=Detalle_ventaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request, "ventas/detalle_venta/crear.html", context)
@login_required
@permission_required("venta.view_detalle_venta", login_url="index")
def detalle_venta_listar(request):
    titulo="Detalle venta"
    modulo="ventas"
    detalle_venta=Detalle_venta.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "detalle_ventas":detalle_venta
    }
    return render(request, "ventas/detalle_venta/listar.html", context)
@login_required
@permission_required("venta.add_change_venta", login_url="index")
def detalle_venta_modificar(request,pk):
    titulo="Detalle venta"
    detalle_venta=Detalle_venta.objects.get(id=pk)
    if request.method== 'POST':
        form= Detalle_ventaUpadteForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('detalle_venta')
    else:
        form= Detalle_ventaUpadteForm(instance=detalle_venta)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "ventas/detalle_venta/modificar.html", context)
@login_required
@permission_required("venta.delete_detalle_venta", login_url="index")
def detalle_venta_eliminar(request,pk):
    detalle_venta= Detalle_venta.objects.filter(id=pk)
    detalle_venta.delete()
    detalle_venta.update(
)
    messages.success(request,'El detalle de venta se elimino correctamente.')
    return redirect('detalle_venta')
#RESERVA
@login_required
@permission_required("venta.add_reserva", login_url="index")
def reserva_crear (request):
    titulo="Reserva"
    if request.method=='POST':
        form=ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('reserva')
    else:
        form=ReservaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request, "ventas/reserva/crear.html", context)
@login_required
@permission_required("venta.view_reserva", login_url="index")
def reserva_listar(request):
    titulo="Reserva"
    modulo="ventas"
    reserva=Reserva.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "reservas":reserva
    }
    return render(request, "ventas/reserva/listar.html", context)
@login_required
@permission_required("venta.change_reserva", login_url="index")
def reserva_modificar(request,pk):
    titulo="Reserva"
    reserva=Reserva.objects.get(id=pk)
    if request.method== 'POST':
        form= ReservaUpdateForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('reserva')
    else:
        form= ReservaUpdateForm(instance=reserva)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "ventas/reserva/modificar.html", context)
@login_required
@permission_required("venta.delete_reserva", login_url="index")
def reserva_eliminar(request,pk):
    reserva= Reserva.objects.filter(id=pk)
    reserva.delete()
    reserva.update(
    )
    messages.success(request,'La reserva se elimino correctamente.')
    return redirect('reserva')
#UBICACION
@login_required
@permission_required("venta.add_ubicacion", login_url="index")
def ubicacion_crear (request):
    titulo="Ubicacion"
    if request.method=='POST':
        form=UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('ubicacion')
    else:
        form=UbicacionForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request, "ventas/ubicacion/crear.html", context)
@login_required
@permission_required("venta.view_ubicacion", login_url="index")
def ubicacion_listar(request):
    titulo="Ubicacion"
    modulo="ventas"
    ubicacion=Ubicacion.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "ubicaciones":ubicacion
    }
    return render(request, "ventas/ubicacion/listar.html", context)
@login_required
@permission_required("venta.change_ubicacion", login_url="index")
def ubicacion_modificar(request,pk):
    titulo="Ubicacion"
    ubicacion=Ubicacion.objects.get(id=pk)
    if request.method== 'POST':
        form= UbicacionUpdateForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('ubicacion')
    else:
        form= UbicacionUpdateForm(instance=ubicacion)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "ventas/ubicacion/modificar.html", context)
@login_required
@permission_required("venta.delete_ubicacion", login_url="index")
def ubicacion_eliminar(request,pk):
    ubicacion= Ubicacion.objects.filter(id=pk)
    ubicacion.delete()
    ubicacion.update(
    )
    messages.success(request,'La ubicación se elimino correctamente.')
    return redirect('ubicacion')
