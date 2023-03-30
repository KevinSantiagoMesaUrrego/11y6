from django import forms

from django.forms import ModelForm, widgets
from usuario.models import Persona,Eps,Turno,Trabajador

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class PersonaUpdateForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        exclude=["documento","rh","fecha_nacimiento"]

class EpsForm(ModelForm):

    class Meta:
        model = Eps
        fields = "__all__"
        exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class EpsUpdateForm(ModelForm):
    class Meta:
        model = Eps
        fields = "__all__"
        exclude=["documento","rh","fecha_nacimiento"]

class TurnoForm(ModelForm):
    
    class Meta:
        model = Turno
        fields = "__all__"
        exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class TurnoUpdateForm(ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"
        exclude=["documento","rh","fecha_nacimiento"]

class TrabajadorForm(ModelForm):
    
    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class TrabajadorUpdateForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude=["documento","rh","fecha_nacimiento"]