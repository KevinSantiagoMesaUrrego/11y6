from django.shortcuts import render, redirect
from usuario.models import Persona
from usuario.models import Eps
from usuario.models import Turno
from usuario.models import Trabajador
from usuario.forms import PersonaForm,PersonaUpdateForm,EpsForm,EpsUpdateForm,TurnoForm,TurnoUpdateForm,TrabajadorForm,TrabajadorUpdateForm
# Create your views here.
def persona_crear(request):
    titulo="Persona"
    if request.method== 'POST':
        form= PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona')
    else:
        form= PersonaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/persona/crear.html", context)

def persona_listar(request):
    titulo="Persona"
    persona= Persona.objects.all()
    context={
        "titulo":titulo,
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
    persona.update(
        estado="0"
    )
    return redirect('persona')


#views de tabla eps
def eps_crear(request):
    titulo="Eps"
    if request.method== 'POST':
        form= EpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eps')
    else:
        form= EpsForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/eps/crear.html", context)

def eps_listar(request):
    titulo="Eps"
    eps= Eps.objects.all()
    context={
        "titulo":titulo,
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
    eps.update(
        estado="0"
    )
    return redirect('eps')

#views de tabla turno
def turno_crear(request):
    titulo="Turno"
    if request.method== 'POST':
        form= TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turno')
    else:
        form= TurnoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/turno/crear.html", context)

def turno_listar(request):
    titulo="Turno"
    turno= Eps.objects.all()
    context={
        "titulo":titulo,
        "turnos":turno
    }
    return render(request,"usuarios/turno/listar.html", context)

def turno_modificar(request,pk):
    titulo="Turno"
    turno= Eps.objects.get(id=pk)
    if request.method== 'POST':
        form= TurnoUpdateForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
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
    turno.update(
        estado="0"
    )
    return redirect('turno')

#views de tabla trabajador
def trabajador_crear(request):
    titulo="Trabajador"
    if request.method== 'POST':
        form= TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajador')
    else:
        form= TrabajadorForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/trabajador/crear.html", context)

def trabajador_listar(request):
    titulo="Trabajador"
    trabajador= Trabajador.objects.all()
    context={
        "titulo":titulo,
        "Trabajadores":trabajador
    }
    return render(request,"usuarios/trabajador/listar.html", context)

def trabajador_modificar(request,pk):
    titulo="Trabajador"
    trabajador= Trabajador.objects.get(id=pk)
    if request.method== 'POST':
        form= TrabajadorUpdateForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajador')
    else:
        form= TrabajadorUpdateForm(instance=trabajador)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/trabajador/modificar.html", context)

def trabajador_eliminar(request,pk):
    usuario= Trabajador.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('trabajador')
