from django.contrib import admin
from usuario.models import Persona, Eps, Trabajador, Turno

# Register your models here.
admin.site.register(Persona)
admin.site.register(Eps)
admin.site.register(Trabajador)
admin.site.register(Turno)

