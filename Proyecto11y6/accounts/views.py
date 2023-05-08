from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from accounts.models import Register

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'partials/register.html', {'form': form})

