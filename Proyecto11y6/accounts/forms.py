from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    correo = forms.EmailField()

    class Meta:
        model = User
        fields = "__all__"
