from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from accounts.models import Register
from accounts.forms import User, Group
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required("register.add_register", login_url="index")
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = form.cleaned_data['group']  # Obtener el grupo seleccionado en el formulario
            messages.success(request, 'La persona se creo correctamente.')
            if group:
                user.groups.add(group)  # Agregar el usuario al grupo seleccionado
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'partials/register.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

@login_required
def vista_protegida(request):
    usuario = request.user
    rol = usuario.rol  # Asume que el modelo de Usuario tiene un campo "rol"

    context = {
        'usuario': usuario,
        'rol': rol,
    }
    return render(request, '../base/templates/index.html', context)
@login_required
@permission_required("persona.view_persona", login_url="index")
def persona_listar(request):
    titulo="Usuarios"
    modulo="Accounts"
    groups_users = {
        "Administrador" : User.objects.filter(groups__name="Administrador"),
        "Cajero" : User.objects.filter(groups__name="Cajero"),
        "Empleado" : User.objects.filter(groups__name="Empleado"),
        "SuperAdministrador": User.objects.filter(is_superuser=True)
    }

    context={
        "titulo":titulo,
        "modulo":modulo,
        "users":groups_users,
    }
    #dd(groups_users)
    return render(request, "usuarios/persona/listar.html", context)
def persona_eliminar(request,pk):
    user= User.objects.filter(id=pk)
    user.update(
        estado="0"
    )
    messages.success(request,'La persona se elimino correctamente.')
    return redirect('persona')
def persona_modificar(request):
    if request.method == 'POST':
        form = PersonaUpdateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = form.cleaned_data['group']  # Obtener el grupo seleccionado en el formulario
            messages.success(request, 'El usuario se creo correctamente.')
            if group:
                user.groups.add(group)  # Agregar el usuario al grupo seleccionado
            return redirect('inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'partials/register.html', {'form': form})

