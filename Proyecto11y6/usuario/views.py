from django.shortcuts import render, redirect
from usuario.models import Persona
from usuario.models import Eps
from usuario.models import Turno
from usuario.models import Trabajador
from usuario.forms import PersonaForm,PersonaUpdateForm
from usuario.forms import EpsForm,EpsUpdateForm
from usuario.forms import TurnoForm,TurnoUpdateForm
from usuario.forms import TrabajadorForm,TrabajadorUpdateForm
# Create your views here.
def persona_crear(request):
    titulo="Persona"
    if request.method== 'POST':
        form= PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= PersonaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def persona_listar(request):
    titulo="Persona"
    usuarios= Persona.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuarios/listar.html", context)

def persona_modificar(request,pk):
    titulo="Persona"
    usuario= Persona.objects.get(id=pk)
    if request.method== 'POST':
        form= PersonaUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= PersonaUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/modificar.html", context)

def persona_eliminar(request,pk):
    usuario= Persona.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')


#views de tabla eps
def eps_crear(request):
    titulo="Usuario"
    if request.method== 'POST':
        form= EpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= EpsForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def eps_listar(request):
    titulo="Eps"
    usuarios= Eps.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuarios/listar.html", context)

def eps_modificar(request,pk):
    titulo="Eps"
    usuario= Eps.objects.get(id=pk)
    if request.method== 'POST':
        form= EpsUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= EpsUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/modificar.html", context)

def eps_eliminar(request,pk):
    usuario= Eps.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')

#views de tabla turno
def turno_crear(request):
    titulo="Turno"
    if request.method== 'POST':
        form= TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= TurnoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def turno_listar(request):
    titulo="Turno"
    usuarios= Eps.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuarios/listar.html", context)

def turno_modificar(request,pk):
    titulo="Turno"
    usuario= Eps.objects.get(id=pk)
    if request.method== 'POST':
        form= TurnoUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= TurnoUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/modificar.html", context)

def turno_eliminar(request,pk):
    usuario= Turno.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')

#views de tabla trabajador
def trabajador_crear(request):
    titulo="Trabajador"
    if request.method== 'POST':
        form= TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= TrabajadorForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def trabajador_listar(request):
    titulo="Trabajador"
    usuarios= Trabajador.objects.all()
    context={
        "titulo":titulo,
        "usuarios":usuarios
    }
    return render(request,"usuarios/listar.html", context)

def trabajador_modificar(request,pk):
    titulo="Trabajador"
    usuario= Trabajador.objects.get(id=pk)
    if request.method== 'POST':
        form= TrabajadorUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= TrabajadorUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/modificar.html", context)

def trabajador_eliminar(request,pk):
    usuario= Trabajador.objects.filter(id=pk)
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')
