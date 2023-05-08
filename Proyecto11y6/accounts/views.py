from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from accounts.models import Register

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            register.activo = False
            return redirect('inicio')
        else:
            messages.error(request, form.error_messages)
            return render(request, 'partials/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'partials/register.html', {'form': form})

