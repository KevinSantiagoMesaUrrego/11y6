from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UpdateUserForm
from accounts.models import Register
from accounts.forms import User, Group
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


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
def persona_listar(request):
    # Verificar si el usuario tiene permisos
    if not request.user.has_perm("persona.view_persona"):
        messages.error(request, "No tienes permisos para acceder a la Lista de Usuarios.")
        return redirect("index")  # Redirige al usuario al índice
    titulo="Persona"
    modulo="Usuarios"
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
def persona_eliminar(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active:
            user.is_active = False  # Desactivar al usuario en lugar de cambiar "estado"
            user.save()
            messages.success(request, 'El usuario se desactivó correctamente.')
        else:
            messages.info(request, 'El usuario ya está inactivo.')
    except User.DoesNotExist:
        messages.error(request, 'No se encontró el usuario a desactivar.')

    return redirect('persona')# Redirige de vuelta a la lista de personas
def persona_modificar(request,pk):
    titulo="Persona"
    persona= User.objects.get(id=pk)
    if request.method== 'POST':
        form= UpdateUserForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha modificado correctamente.')
            return redirect('persona')
    else:
        form= UpdateUserForm(instance=persona)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request, "usuarios/persona/modificar.html", context)



