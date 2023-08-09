from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def vista_protegida(request):
    usuario = request.user
    rol = usuario.rol  # Asume que el modelo de Usuario tiene un campo "rol"

    context = {
        'usuario': usuario,
        'rol': rol,
    }
    return render(request, 'index.html', context)
@login_required
def persona_listar(request):
    titulo="Usuarios"
    modulo="Accounts"
    groups_users = {
        "Administrador" : User.objects.filter(groups__name="Administrador"),
        "Cajero" : User.objects.filter(groups__name="Cajero"),
        "Empleado" : User.objects.filter(groups__name="Empleado"),
    }

    context={
        "titulo":titulo,
        "modulo":modulo,
        "users":groups_users,
    }
    #dd(groups_users)
    return render(request,"usuarios/persona/listar.html", context)


