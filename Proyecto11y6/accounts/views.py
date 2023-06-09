from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from accounts.models import Register
from django.contrib.auth import logout
from django.template import RequestContext

def register(request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            register.activo = False
            return redirect('inicio')
        else:
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


