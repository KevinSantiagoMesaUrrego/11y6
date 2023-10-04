from django import forms

from django.forms import ModelForm, widgets
from usuario.models import Persona, Eps, Turno, Trabajador
from compra.models import Personalizacion

class PersonalizarForm(forms.ModelForm):
    class Meta:
        model = Personalizacion
        fields = "__all__"
        exclude = ["estado"]
class PersonalizarUpdateForm(ModelForm):
    class Meta:
        model = Personalizacion
        fields = "__all__"
        exclude = ["estado"]

class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = ["estado"]


class PersonaUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = ["estado"]


class EpsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Eps
        fields = "__all__"
        exclude = ["estado"]


class EpsUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Eps
        fields = "__all__"
        exclude = ["estado"]


class TurnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Turno
        fields = "__all__"
        widgets = {
            'fecha_ingreso': widgets.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_salida': widgets.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ["estado", ]


class TurnoUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Turno
        fields = "__all__"
        widgets = {
            'fecha_ingreso': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_salida': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ["estado", ]


class TrabajadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude = ["estado"]

        # fields= ["nombre","apellido","documento","tipoDocumento"]


class TrabajadorUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Trabajador
        fields = "__all__"
        exclude = ["estado"]
