from django import forms

from django.forms import ModelForm, widgets
from usuario.models import Persona,Eps,Turno,Trabajador


class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            #visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Persona
        fields = "__all__"
        exclude=["estado"]

class PersonaUpdateForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        exclude=["estado"]

class EpsForm(ModelForm):

    class Meta:
        model = Eps
        fields = "__all__"
        exclude=["estado"]
class EpsUpdateForm(ModelForm):
    class Meta:
        model = Eps
        fields = "__all__"
        exclude=["estado"]

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"
        widgets={
            'fecha_ingreso': widgets.DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M'),
            'fecha_salida': widgets.DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M'),
        }
        exclude=["estado",]
class TurnoUpdateForm(ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"
        widgets={
            'fecha_ingreso': widgets.DateTimeInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M'),
            'fecha_salida': widgets.DateTimeInput(attrs={'type':'datetime-local'},format='%Y-%m-%dT%H:%M'),
        }
        exclude=["estado",]
class TrabajadorForm(ModelForm):
    
    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude=["estado"]

        # fields= ["nombre","apellido","documento","tipoDocumento"]
class TrabajadorUpdateForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude=["estado"]
