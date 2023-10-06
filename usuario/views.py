from django.shortcuts import render, redirect
from usuario.models import Eps
from usuario.models import Turno
from usuario.models import Trabajador
from usuario.forms import EpsForm,EpsUpdateForm,TurnoForm,TurnoUpdateForm,TrabajadorForm,TrabajadorUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

#views de tabla eps
@login_required
@permission_required("usuario.add_eps", login_url="index")
def eps_crear(request):
    titulo="Eps"
    if request.method== 'POST':
        form= EpsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La eps se creo correctamente.')
            return redirect('eps')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= EpsForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/eps/crear.html", context)
@login_required
def eps_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.view_eps"):
        messages.error(request, "No tienes permisos para acceder a Eps.")
        return redirect("index")  # Redirige al usuario al índice
    titulo="Eps"
    modulo="Usuarios"
    eps= Eps.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "eps":eps
    }
    return render(request, "usuarios/eps/listar.html", context)
@login_required
@permission_required("usuario.change_eps", login_url="index")
def eps_modificar(request,pk):
    titulo="Eps"
    eps= Eps.objects.get(id=pk)
    if request.method== 'POST':
        form= EpsUpdateForm(request.POST, instance=eps)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modifico correctamente.')
            return redirect('eps')
    else:
        form= EpsUpdateForm(instance=eps)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/eps/modificar.html", context)
@login_required
@permission_required("usuario.delete_eps", login_url="index")
def eps_eliminar(request,pk):
    eps= Eps.objects.filter(id=pk)
    eps.update(
        estado="0"
    )
    messages.success(request,'La eps se elimino correctamente.')
    return redirect('eps')

#views de tabla turno
@login_required
def turno_crear(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.add_turno"):
        messages.error(request, "No tienes permisos para Crear un Turno.")
        return redirect("turno")  # Redirige al usuario al índice
    titulo="Turno"
    if request.method== 'POST':
        form= TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El turno se creo correctamente.')
            return redirect('turno')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= TurnoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/turno/crear.html", context)
@login_required
def turno_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.view_turno"):
        messages.error(request, "No tienes permisos para acceder a Turno.")
        return redirect("index")  # Redirige al usuario al índice
    titulo="Turno"
    modulo="Usuarios"
    turnos= Turno.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "turnos":turnos
    }
    return render(request, "usuarios/turno/listar.html", context)
@login_required
def turno_modificar(request,pk):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.change_turno"):
        messages.error(request, "No tienes permisos para modificar el Turno.")
        return redirect("turno")  # Redirige al usuario al índice
    titulo="Turno"
    turno= Turno.objects.get(id=pk)
    if request.method== 'POST':
        form= TurnoUpdateForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modificado correctamente.')
            return redirect('turno')
    else:
        form= TurnoUpdateForm(instance=turno)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/turno/modificar.html", context)
@login_required
def turno_eliminar(request,pk):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.delete_turno"):
        messages.error(request, "No tienes permisos para eliminar el Turno.")
        return redirect("turno")  # Redirige al usuario al índice
    turno= Turno.objects.filter(id=pk)
    turno.update(
        estado="0"
    )
    messages.success(request,'El turno se elimino correctamente.')
    return redirect('turno')

#views de tabla trabajador
@login_required
@permission_required("usuario.add_trabajador", login_url="index")
def trabajador_crear(request):
    titulo="Trabajador"
    if request.method== 'POST':
        form= TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'El trabajador se creo correctamente.')
            return redirect('trabajador')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= TrabajadorForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/trabajador/crear.html", context)
@login_required
def trabajador_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("usuario.view_trabajador"):
        messages.error(request, "No tienes permisos para acceder a los datos del Trabajador.")
        return redirect("index")  # Redirige al usuario al índice
    titulo="Trabajador"
    modulo="Usuarios"
    trabajadores= Trabajador.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "trabajadores":trabajadores
    }
    return render(request, "usuarios/trabajador/listar.html", context)
@login_required
@permission_required("usuario.change_trabajador", login_url="index")
def trabajador_modificar(request,pk):
    titulo="Trabajador"
    trabajador= Trabajador.objects.get(id=pk)
    if request.method== 'POST':
        form= TrabajadorUpdateForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se modificado correctamente.')
            return redirect('trabajador')
    else:
        form= TrabajadorUpdateForm(instance=trabajador)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/trabajador/modificar.html", context)
@login_required
@permission_required("usuario.delete_trabajador", login_url="index")
def trabajador_eliminar(request,pk):
    trabajador= Trabajador.objects.filter(id=pk)
    trabajador.update(
        estado="0"
    )
    messages.success(request,'El trabajador se elimino correctamente.')
    return redirect('trabajador')
