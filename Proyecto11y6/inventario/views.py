from django.shortcuts import render,redirect
from inventario.models import Producto,Marca,Presentacion,Unidad_medida,Consumo_trabajador
from inventario.forms import Productoform,ProductoUpdateForm,Marcaform,MarcaUpdateForm,Presentacionform,PresentacionUpdateForm,Unidad_medidaform,Unidad_medidaUpdateForm,Consumo_trabjadorform,Consumo_trabajadorUpdateForm

# Create your views here.

#PRODUCTO
def producto_crear (request):
    titulo="Producto"
    if request.method=='POST':
        form=Productoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form=Productoform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/producto/crear.html",context)

def producto_listar(request):
    titulo="Producto"
    modulo="productos"
    producto=Producto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "productos":producto
    }
    return render(request,"inventarios/producto/listar.html",context)

def producto_modificar(request,pk):
    titulo="Producto"
    producto=Producto.objects.get(id=pk)
    if request.method=='POST':
        form=ProductoUpdateForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/producto/modificar.html", context)

def producto_eliminar(request,pk):
    producto= Producto.objects.filter(id=pk)
    producto.delete()
    producto.update(
    )
    return redirect('producto')

#MARCA
def marca_crear (request):
    titulo="Marca"
    if request.method=='POST':
        form=Marcaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca')
    else:
        form=Marcaform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/marca/crear.html",context)

def marca_listar(request):
    titulo="Marca"
    modulo="marcas"
    marca=Marca.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "marcas":marca
    }
    return render(request,"inventarios/marca/listar.html",context)

def marca_modificar(request,pk):
    titulo="Marca"
    marca=Marca.objects.get(id=pk)
    if request.method=='POST':
        form=MarcaUpdateForm(request.POST,instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca')
    else:
        form= MarcaUpdateForm(instance=marca)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/marca/modificar.html", context)

def marca_eliminar(request,pk):
    marca= Marca.objects.filter(id=pk)
    marca.delete()
    marca.update(
    )
    return redirect('marca')

#PRESENTACION
def presentacion_crear (request):
    titulo="Presentacion"
    if request.method=='POST':
        form=Presentacionform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presentacion')
    else:
        form=Presentacionform()
    context={
        "titulo":titulo,
        "form":form,
    }
    return render(request,"inventarios/presentacion/crear.html",context)

def presentacion_listar(request):
    titulo="Presentacion"
    modulo="presentaciones"
    presentacion=Presentacion.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "presentaciones":presentacion
    }
    return render(request,"inventarios/presentacion/listar.html",context)

def presentacion_modificar(request,pk):
    titulo="Presentacion"
    presentacion=Presentacion.objects.get(id=pk)
    if request.method=='POST':
        form=PresentacionUpdateForm(request.POST,instance=presentacion)
        if form.is_valid():
            form.save()
            return redirect('presentacion')
    else:
        form= PresentacionUpdateForm(instance=presentacion)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/presentacion/modificar.html", context)

def presentacion_eliminar(request,pk):
    presentacion= Presentacion.objects.filter(id=pk)
    presentacion.delete()
    presentacion.update(
    )
    return redirect('presentacion')

#UNIDADMEDIDA
def unidadmedida_crear (request):
    titulo="UnidadMedida"
    if request.method=='POST':
        form=Unidad_medidaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidadmedida')
    else:
        form=Unidad_medidaform()
    context={
        "titulo":titulo,
        "form":form,
        }
    return render(request,"inventarios/unidad_medida/crear.html",context)

def unidadmedida_listar(request):
    titulo="UnidadMedida"
    modulo="unidadmedidas"
    unidadmedida=Unidad_medida.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "unidadmedidas":unidadmedida
    }
    return render(request,"inventarios/unidad_medida/listar.html",context)

def unidadmedida_modificar(request,pk):
    titulo="UnidadMedida"
    unidadmedida=Unidad_medida.objects.get(id=pk)
    if request.method=='POST':
        form=Unidad_medidaUpdateForm(request.POST,instance=unidadmedida)
        if form.is_valid():
            form.save()
            return redirect('unidadmedida')
    else:
        form= Unidad_medidaUpdateForm(instance=unidadmedida)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/unidad_medida/modificar.html", context)

def unidadmedida_eliminar(request,pk):
    unidadmedida= Unidad_medida.objects.filter(id=pk)
    unidadmedida.delete()
    unidadmedida.update(
    )
    return redirect('unidadmedida')

#CONSUMOTRABAJADOR
def consumotrabajador_crear (request):
    titulo="ConsumoTrabajador"
    if request.method=='POST':
        form=Consumo_trabjadorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumotrabajador')
    else:
        form=Consumo_trabjadorform()
    context={
        "titulo":titulo,
        "form":form,
        }
    return render(request,"inventarios/consumo_trabajador/crear.html",context)

def consumotrabajador_listar(request):
    titulo="ConsumoTrabajador"
    modulo="consumotrabajadores"
    consumotrabajador=Consumo_trabajador.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "consumotrabajadores":consumotrabajador
    }
    return render(request,"inventarios/consumo_trabajador/listar.html",context)

def consumotrabajador_modificar(request,pk):
    titulo="ConsumoTrabajador"
    consumotrabajador=Consumo_trabajador.objects.get(id=pk)
    if request.method=='POST':
        form=Consumo_trabajadorUpdateForm(request.POST,instance=consumotrabajador)
        if form.is_valid():
            form.save()
            return redirect('consumotrabajador')
    else:
        form= Consumo_trabajadorUpdateForm(instance=consumotrabajador)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"inventarios/consumo_trabajador/modificar.html", context)

def consumotrabajador_eliminar(request,pk):
    consumotrabajador= Consumo_trabajador.objects.filter(id=pk)
    consumotrabajador.delete()
    consumotrabajador.update(
    )
    return redirect('consumotrabajador')




