from django.shortcuts import render,redirect
from inventario.models import Producto,Marca,Presentacion,UnidadMedida,ConsumoTrabajador
from inventario.forms import Productoform,ProductoUpdateForm,Marcaform,MarcaUpdateForm,Presentacionform,PresentacionUpdateForm,UnidadMedidaform,UnidadMedidaUpdateForm,ConsumoTrabjadorform,ConsumoTrabajadorUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

#PRODUCTO
@login_required
@permission_required("inventario.add_producto", login_url="index")
def producto_crear (request):
    titulo="Producto"
    if request.method=='POST':
        form=Productoform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('producto')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=Productoform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/producto/crear.html",context)
@login_required
@permission_required("inventario.view_producto", login_url="index")
def producto_listar(request):
    titulo="Producto"
    modulo="inventarios"
    producto=Producto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "productos":producto
    }
    return render(request,"inventarios/producto/listar.html",context)
@login_required
@permission_required("inventario.change_producto", login_url="index")
def producto_modificar(request,pk):
    titulo="Producto"
    producto=Producto.objects.get(id=pk)
    if request.method=='POST':
        form=ProductoUpdateForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('producto')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/producto/modificar.html", context)
@login_required
@permission_required("inventario.delete_producto", login_url="index")
def producto_eliminar(request,pk):
    producto= Producto.objects.filter(id=pk)
    producto.delete()
    producto.update(
    )
    messages.success(request,'El producto se elimino correctamente.')
    return redirect('producto')

#MARCA
@login_required
@permission_required("inventario.add_marca", login_url="index")
def marca_crear (request):
    titulo="Marca"
    if request.method=='POST':
        form=Marcaform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('marca')
        else:
            messages.error(request, 'El formulario tiene errores.')
            
    else:
        form=Marcaform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/marca/crear.html",context)
@login_required
@permission_required("inventario.view_marca", login_url="index")
def marca_listar(request):
    titulo="Marca"
    modulo="inventarios"
    marca=Marca.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "marcas":marca
    }
    return render(request,"inventarios/marca/listar.html",context)
@login_required
@permission_required("inventario.change_marca", login_url="index")
def marca_modificar(request,pk):
    titulo="Marca"
    marca=Marca.objects.get(id=pk)
    if request.method=='POST':
        form=MarcaUpdateForm(request.POST,instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('marca')
    else:
        form= MarcaUpdateForm(instance=marca)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/marca/modificar.html", context)
@login_required
@permission_required("inventario.delete_marca", login_url="index")
def marca_eliminar(request,pk):
    marca= Marca.objects.filter(id=pk)
    marca.delete()
    marca.update(
    )
    messages.success(request,'La marca se elimino correctamente.')
    return redirect('marca')

#PRESENTACION
@login_required
@permission_required("inventario.add_presentacion", login_url="index")
def presentacion_crear (request):
    titulo="Presentacion"
    if request.method=='POST':
        form=Presentacionform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('presentacion')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=Presentacionform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/presentacion/crear.html",context)
@login_required
@permission_required("inventario.view_presentacion", login_url="index")
def presentacion_listar(request):
    titulo="Presentacion"
    modulo="inventarios"
    presentacion=Presentacion.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "presentaciones":presentacion
    }
    return render(request,"inventarios/presentacion/listar.html",context)
@login_required
@permission_required("inventario.change_presentacion", login_url="index")
def presentacion_modificar(request,pk):
    titulo="Presentacion"
    presentacion=Presentacion.objects.get(id=pk)
    if request.method=='POST':
        form=PresentacionUpdateForm(request.POST,instance=presentacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('presentacion')
    else:
        form= PresentacionUpdateForm(instance=presentacion)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/presentacion/modificar.html", context)
@login_required
@permission_required("inventario.delete_presentacion", login_url="index")
def presentacion_eliminar(request,pk):
    presentacion= Presentacion.objects.filter(id=pk)
    presentacion.delete()
    presentacion.update(
    )
    messages.success(request,'La presentación se elimino correctamente.')
    return redirect('presentacion')

#UNIDADMEDIDA
@login_required
@permission_required("inventario.add_unidad_medida", login_url="index")
def unidadmedida_crear (request):
    titulo="Unidad Medida"
    if request.method=='POST':
        form=UnidadMedidaform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('unidadmedida')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=UnidadMedidaform()
    context={
        "titulo":titulo,
        "form":form,
        }
    return render(request,"inventarios/unidad_medida/crear.html",context)
@login_required
@permission_required("inventario.view_unidad_medida", login_url="index")
def unidadmedida_listar(request):
    titulo="Unidad Medida"
    modulo="inventarios"
    unidadmedida=UnidadMedida.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "unidadmedidas":unidadmedida
    }
    return render(request,"inventarios/unidad_medida/listar.html",context)
@login_required
@permission_required("inventario.change_unidad_medida", login_url="index")
def unidadmedida_modificar(request,pk):
    titulo="Unidad Medida"
    unidadmedida=UnidadMedida.objects.get(id=pk)
    if request.method=='POST':
        form=UnidadMedidaUpdateForm(request.POST,instance=unidadmedida)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('unidadmedida')
    else:
        form= UnidadMedidaUpdateForm(instance=unidadmedida)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/unidad_medida/modificar.html", context)
@login_required
@permission_required("inventario.delete_unidad_medida", login_url="index")
def unidadmedida_eliminar(request,pk):
    unidadmedida= UnidadMedida.objects.filter(id=pk)
    unidadmedida.delete()
    unidadmedida.update(
    )
    messages.success(request,'La unidad de medida se elimino correctamente.')
    return redirect('unidadmedida')

#CONSUMOTRABAJADOR
@login_required
@permission_required("inventario.add_consumo_trabajador", login_url="index")
def consumotrabajador_crear (request):
    titulo="Consumo Trabajador"
    if request.method=='POST':
        form=ConsumoTrabjadorform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creo correctamente.')
            return redirect('consumotrabajador')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form=ConsumoTrabjadorform()
    context={
        "titulo":titulo,
        "form":form,
        }
    return render(request,"inventarios/consumo_trabajador/crear.html",context)
@login_required
@permission_required("inventario.view_consumo_trabajador", login_url="index")
def consumotrabajador_listar(request):
    titulo="Consumo Trabajador"
    modulo="inventarios"
    consumotrabajador=ConsumoTrabajador.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "consumotrabajadores":consumotrabajador
    }
    return render(request,"inventarios/consumo_trabajador/listar.html",context)
@login_required
@permission_required("inventario.change_consumo_trabajador", login_url="index")
def consumotrabajador_modificar(request,pk):
    titulo="Consumo Trabajador"
    consumotrabajador=ConsumoTrabajador.objects.get(id=pk)
    if request.method=='POST':
        form=ConsumoTrabajadorUpdateForm(request.POST,instance=consumotrabajador)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('consumotrabajador')
    else:
        form= ConsumoTrabajadorUpdateForm(instance=consumotrabajador)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/consumo_trabajador/modificar.html", context)
@login_required
@permission_required("inventario.delete_consumo_trabajador", login_url="index")
def consumotrabajador_eliminar(request,pk):
    consumotrabajador= ConsumoTrabajador.objects.filter(id=pk)
    consumotrabajador.delete()
    consumotrabajador.update(
    )
    messages.success(request,'El consumo de trabajador se elimino correctamente.')
    return redirect('consumotrabajador')




