from django.shortcuts import render, redirect
from usuario.models import Persona
from usuario.models import Eps
from usuario.models import Turno
from usuario.models import Trabajador
from usuario.forms import PersonaForm,PersonaUpdateForm,EpsForm,EpsUpdateForm,TurnoForm,TurnoUpdateForm,TrabajadorForm,TrabajadorUpdateForm
from django.contrib import messages
# Create your views here.
def persona_crear(request):
    titulo="Persona"
    if request.method== 'POST':
        form= PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'La persona se creo correctamente.')
            return redirect('persona')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= PersonaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/persona/crear.html", context)

def persona_listar(request):
    titulo="Persona"
    modulo="Usuarios"
    persona= Persona.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "personas":persona
    }
    return render(request,"usuarios/persona/listar.html", context)

def persona_modificar(request,pk):
    titulo="Persona"
    persona= Persona.objects.get(id=pk)
    if request.method== 'POST':
        form= PersonaUpdateForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('persona')
    else:
        form= PersonaUpdateForm(instance=persona)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/persona/modificar.html", context)

def persona_eliminar(request,pk):
    persona= Persona.objects.filter(id=pk)
    persona.delete()
    persona.update()
    return redirect('persona')


#views de tabla eps
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
    return render(request,"usuarios/eps/crear.html", context)

def eps_listar(request):
    titulo="Eps"
    modulo="Usuarios"
    eps= Eps.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "eps":eps
    }
    return render(request,"usuarios/eps/listar.html", context)

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
    return render(request,"usuarios/eps/modificar.html", context)

def eps_eliminar(request,pk):
    eps= Eps.objects.filter(id=pk)
    eps.delete()
    eps.update()
    return redirect('eps')

#views de tabla turno
def turno_crear(request):
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
    return render(request,"usuarios/turno/crear.html", context)

def turno_listar(request):
    titulo="Turno"
    modulo="Usuarios"
    turnos= Turno.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "turnos":turnos
    }
    return render(request,"usuarios/turno/listar.html", context)

def turno_modificar(request,pk):
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
    return render(request,"usuarios/turno/modificar.html", context)

def turno_eliminar(request,pk):
    turno= Turno.objects.filter(id=pk)
    turno.delete()
    turno.update()
    return redirect('turno')

#views de tabla trabajador
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
    return render(request,"usuarios/trabajador/crear.html", context)

def trabajador_listar(request):
    titulo="Trabajador"
    modulo="Usuarios"
    trabajadores= Trabajador.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "trabajadores":trabajadores
    }
    return render(request,"usuarios/trabajador/listar.html", context)

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
    return render(request,"usuarios/trabajador/modificar.html", context)

def trabajador_eliminar(request,pk):
    trabajador= Trabajador.objects.filter(id=pk)
    trabajador.delete()
    trabajador.update()
    return redirect('trabajador')
