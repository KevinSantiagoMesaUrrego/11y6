from django.shortcuts import render,redirect,get_object_or_404
from compra.models import Compra,Detalle_compra,Proveedor,Evento
from compra.forms import CompraForm,CompraUpdateForm,Detalle_compraForm,Detalle_compraUpdateForm,ProveedorForm,ProveedorUpdateForm,EventoForm,EventoUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from inventario.models import Producto


# Create your views here.

@login_required
@permission_required("compra.add_compra", login_url="index")
def compra_crear(request):
    titulo = "Compra"
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            messages.success(request,'La Compra se creo correctamente.')
            return redirect('detalle_compra', pk=compra.id)
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form = CompraForm()
    context = {
        "titulo": titulo,
        "form": form,
    }
    return render(request, "compras/compra/crear.html", context)
@login_required
def compra_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("compra.view_compra"):
        messages.error(request, "No tienes permisos para acceder a Compra.")
        return redirect("index")  # Redirige al usuario al índice
    titulo = "Compra"
    modulo="compras"
    compra=Compra.objects.all()
    context = {
        "titulo": titulo,
        "modulo":modulo,
        "compras": compra
    }
    return render(request, "compras/compra/listar.html", context)

@login_required
@permission_required("compra.change_compra", login_url="index")
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

@login_required
@permission_required("compra.delete_compra", login_url="index")
def compra_eliminar(request, pk):
    compra = Compra.objects.filter(id=pk)
    compra.delete()
    compra.update(

    )
    messages.success(request,'La compra se elimino correctamente.')
    return redirect('compra')


# views de tabla detalle_compra
@login_required
@permission_required("compra.add_detalle_compra", login_url="index")
def detalle_compra_crear(request):
    titulo = "Detalle compra"
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

@login_required
def detalle_compra_listar(request,pk):
    if not request.user.has_perm("compra.view_detalle_compra"):
        messages.error(request, "No tienes permisos para acceder al Detalle de la Compra.")
        return redirect("index")  # Redirige al usuario al índice
    titulo = "Detalle Compra"
    modulo = "compras"
    compra = Compra.objects.get(id=pk)
    productos = Producto.objects.filter(estado="1")
    detalle_compras = Detalle_compra.objects.filter(compra_id=pk)
    if request.method == "POST":
        form = Detalle_compraForm(request.POST)
        if form.is_valid():
            det_compra = form.save(commit=False)
            det_compra.compra = compra
            det_compra.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_compra", pk)
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_compraForm()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "detalle_compras": detalle_compras,
        "user": request.user,
        "compra": compra,
        "productos": productos,
    }
    return render(request, "compras/detalle_compra/listar.html", context)

@login_required
@permission_required("compra.change_detalle_compra", login_url="index")
def detalle_compra_modificar(request, pk):
    titulo = "Detalle compra"
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

@login_required
@permission_required("compra.delete_detalle_compra", login_url="index")
def detalle_compra_eliminar(request, pk):
    detalle_compra = Detalle_compra.objects.filter(id=pk)
    detalle_compra.delete()
    detalle_compra.update()
    messages.success(request,'El detalle de compra se elimino correctamente.')
    return redirect('detalle_compra')

# views de tabla evento

@login_required
@permission_required("compra.add_evento", login_url="index")
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

@login_required
def evento_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("compra.view_evento"):
        messages.error(request, "No tienes permisos para acceder a los Eventos.")
        return redirect("index")  # Redirige al usuario al índice
    titulo = "Evento"
    modulo="compras"
    evento = Evento.objects.all()
    context = {
        "titulo": titulo,
        "modulo":modulo,
        "eventos": evento

    }
    return render(request, "compras/evento/listar.html", context)

@login_required
@permission_required("compra.change_evento", login_url="index")
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

@login_required
@permission_required("compra.delete_evento", login_url="index")
def evento_eliminar(request, pk):
    evento = Evento.objects.filter(id=pk)
    evento.delete()
    evento.update(
        estado_evento="0"
    )
    messages.success(request,'El evento se elimino correctamente.')
    return redirect('evento')

# views de tabla Proveedor

@login_required
@permission_required("compra.add_proveedor", login_url="index")
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

@login_required
def proveedor_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("compra.view_proveedor"):
        messages.error(request, "No tienes permisos para acceder a la Lista de Proveedores.")
        return redirect("index")  # Redirige al usuario al índice
    titulo = "Proveedor"
    modulo="compras"
    proveedor = Proveedor.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "proveedores":proveedor
    }
    return render(request, "compras/proveedor/listar.html", context)

@login_required
@permission_required("compra.change_proveedor", login_url="index")
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

def compra_finalizar(request, pk):
    compra = Compra.objects.filter(id=pk)
    compra.update(estado_compra="0")  # Actualizar el campo correcto
    return redirect("/compras/compra")


@login_required
@permission_required("compra.delete_proveedor", login_url="index")
def proveedor_eliminar(request, pk):
    proveedor = Proveedor.objects.filter(id=pk)
    proveedor.delete()
    proveedor.update(
    )
    messages.success(request,'El proveedor se elimino correctamente...')
    return redirect('proveedor')

def ver_detalle(request,pk):
    compra=Compra.objects.get(pk=pk)
    detalle_compra=Detalle_compra.objects.filter(compra=compra)
    context = {
        'titulo': 'Titulo de la compra',
        'compra' : compra,
        "detalle_compras":detalle_compra,
    }
    return render(request, 'compras/compra/compra_final.html', context)
def eliminar_detalle_compra(request,pk):
    detalle_compra=get_object_or_404(Detalle_compra,id=pk)
    detalle_compra.delete()
    messages.success(request, 'el producto se elimino correctamente.')
    return redirect('detalle_compra',pk=detalle_compra.compra.pk)