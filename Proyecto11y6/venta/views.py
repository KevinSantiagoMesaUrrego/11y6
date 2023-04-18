from django.shortcuts import render,redirect
from venta.models import Venta,Detalle_venta,Reserva,Ubicacion
from venta.forms import VentaForm,VentaUpadteForm,Detalle_ventaForm,Detalle_ventaUpadteForm,ReservaForm,ReservaUpdateForm,UbicacionForm,UbicacionUpdateForm
# Create your views here.
#VENTA
def venta_crear (request):
    titulo="Venta"
    if request.method=='POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form=VentaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"venta/crear.html",context)
def venta_listar(request):
    titulo="Venta"
    venta=Venta.objects.all()
    context={
        "titulo":titulo,
        "venta":venta
    }
    return render(request,"venta/listar.html",context)
def venta_modificar(request,pk):
    titulo="Venta"
    venta=Venta.objects.get(id=pk)
    if request.method== 'POST':
        form= VentaUpadteForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= VentaUpadteForm(instance=venta)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"venta/modificar.html", context)
def venta_eliminar(request,pk):
    venta= Venta.objects.filter(id=pk)
    venta.update(
    )
    return redirect('venta')
#DETALLE VENTA
def detalle_venta_crear (request):
    titulo="Detalle_venta"
    if request.method=='POST':
        form=Detalle_ventaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta')
    else:
        form=Detalle_ventaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"ventas/detalle_venta/crear.html",context)
def detalle_venta_listar(request):
    titulo="Detalle_venta"
    detalle_venta=Detalle_venta.objects.all()
    context={
        "titulo":titulo,
        "venta":detalle_venta
    }
    return render(request,"ventas/detalle_venta/listar.html",context)
def detalle_venta_modificar(request,pk):
    titulo="Detalle_venta"
    detalle_venta=Detalle_venta.objects.get(id=pk)
    if request.method== 'POST':
        form= VentaUpadteForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= Detalle_ventaUpadteForm(instance=detalle_venta)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"venta/modificar.html", context)
def detalle_venta_eliminar(request,pk):
    detalle_venta= Detalle_venta.objects.filter(id=pk)
    detalle_venta.delete()
    detalle_venta.update(
    )
    return redirect('venta')
#RESERVA
def reserva_crear (request):
    titulo="Reserva"
    if request.method=='POST':
        form=ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form=ReservaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"venta/crear.html",context)
def reserva_listar(request):
    titulo="Reserva"
    reserva=Reserva.objects.all()
    context={
        "titulo":titulo,
        "venta":reserva
    }
    return render(request,"venta/listar.hmtl",context)
def reserva_modificar(request,pk):
    titulo="Reserva"
    reserva=Reserva.objects.get(id=pk)
    if request.method== 'POST':
        form= VentaUpadteForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= ReservaUpdateForm(instance=reserva)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"venta/modificar.html", context)
def reserva_eliminar(request,pk):
    reserva= Reserva.objects.filter(id=pk)
    reserva.update(
    )
    return redirect('venta')
#UBICACION
def ubicacion_crear (request):
    titulo="Reserva"
    if request.method=='POST':
        form=UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form=UbicacionForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"venta/crear.html",context)
def ubicacion_listar(request):
    titulo="Ubicacion"
    ubicacion=Reserva.objects.all()
    context={
        "titulo":titulo,
        "venta":ubicacion
    }
    return render(request,"venta/listar.hmtl",context)
def ubicacion_modificar(request,pk):
    titulo="Ubicacion"
    ubicacion=Ubicacion.objects.get(id=pk)
    if request.method== 'POST':
        form= VentaUpadteForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form= ReservaUpdateForm(instance=ubicacion)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"venta/modificar.html", context)
def ubicacion_eliminar(request,pk):
    reserva= Reserva.objects.filter(id=pk)
    reserva.update(
    )
    return redirect('venta')
