from django.shortcuts import render, redirect
from compra.models import Compra
from compra.models import Detalle_compra
from compra.models import Evento
from compra.models import Proveedor
from compra.forms import CompraForm, CompraUpdateForm, Detalle_compraForm, Detalle_compraUpdateForm, EventoForm, EventoUpdateForm, ProveedorForm, ProveedorUpdateForm
from django.contrib import messages
# Create your views here.


def compra_crear(request):
    titulo = "Compra"
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La Compra se creo correctamente.')
            return redirect('compra')
        else:
            messages.error(request, 'El formulario tiene errores.')
            return redirect('compra')
    else:
        form = CompraForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/compra/crear.html", context)


def compra_listar(request):
    titulo = "Compra"
    modulo="compras"
    compra = Compra.objects.all()
    context = {
        "titulo": titulo,
        "modulo":modulo,
        "compras": compra
    }
    return render(request, "compras/compra/listar.html", context)


def compra_modificar(request, pk):
    titulo = "Compra"
    compra = Compra.objects.get(id=pk)
    if request.method == 'POST':
        form = CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('compra')
    else:
        form = CompraUpdateForm(instance=compra)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/compra/modificar.html", context)


def compra_eliminar(request, pk):
    compra = Compra.objects.filter(id=pk)
    compra.delete()
    compra.update(

    )
    return redirect('compra')


# views de tabla detalle_compra
def detalle_compra_crear(request):
    titulo = "Detalle_compra"
    if request.method == 'POST':
        form = Detalle_compraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El Detalle de compra se creo correctamente.')
            return redirect('detalle_compra')
        else:
            messages.error(request, 'El formulario tiene errores.')
            return redirect('detalle_compra')
    else:
        form = Detalle_compraForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/detalle_compra/crear.html", context)


def detalle_compra_listar(request):
    titulo = "Detalle_compra"
    modulo="compras"
    detalle_compra = Detalle_compra.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "detalle_compras": detalle_compra
    }
    return render(request, "compras/detalle_compra/listar.html", context)


def detalle_compra_modificar(request, pk):
    titulo = "Detalle_compra"
    detalle_compra = Detalle_compra.objects.get(id=pk)
    if request.method == 'POST':
        form = Detalle_compraUpdateForm(request.POST, instance=detalle_compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('detalle_compra')
    else:
        form = Detalle_compraUpdateForm(instance=detalle_compra)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/detalle_compra/modificar.html", context)


def detalle_compra_eliminar(request, pk):
    detalle_compra = Detalle_compra.objects.filter(id=pk)
    detalle_compra.delete()
    detalle_compra.update()
        
    return redirect('detalle_compra')

# views de tabla evento


def evento_crear(request):
    titulo = "Evento"
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El Evento se creo correctamente.')
            return redirect('evento')
        else:
            messages.error(request, 'El formulario tiene errores.')
            return redirect('evento')
    else:
        form = EventoForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/evento/crear.html", context)


def evento_listar(request):
    titulo = "Evento"
    modulo="compras"
    evento = Evento.objects.all()
    context = {
        "titulo": titulo,
        "modulo":modulo,
        "eventos": evento

    }
    return render(request, "compras/evento/listar.html", context)


def evento_modificar(request, pk):
    titulo = "Evento"
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        form = EventoUpdateForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('evento')
    else:
        form = EventoUpdateForm(instance=evento)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/evento/modificar.html", context)


def evento_eliminar(request, pk):
    evento = Evento.objects.filter(id=pk)
    evento.delete()
    evento.update(
        estado_evento="0"
    )
    return redirect('evento')

# views de tabla Proveedor


def proveedor_crear(request):
    titulo = "Proveedor"
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El Proveedor se creo correctamente.')
            return redirect('proveedor')
        else:
            messages.error(request, 'El formulario tiene errores.')
            return redirect('proveedor')
    else:
        form = ProveedorForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/proveedor/crear.html", context)


def proveedor_listar(request):
    titulo = "Proveedor"
    modulo="compras"
    proveedor = Proveedor.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "proveedores":proveedor
    }
    return render(request, "compras/proveedor/listar.html", context)


def proveedor_modificar(request, pk):
    titulo = "Proveedor"
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        form = ProveedorUpdateForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('proveedor')
    else:
        form = ProveedorUpdateForm(instance=proveedor)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "compras/proveedor/modificar.html", context)


def proveedor_eliminar(request, pk):
    proveedor = Proveedor.objects.filter(id=pk)
    proveedor.delete()
    proveedor.update(
    )
    return redirect('proveedor')
