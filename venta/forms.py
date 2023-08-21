from django import forms
from django.forms import ModelForm, widgets
from venta.models import Venta, Detalle_venta, Reserva, Ubicacion


# VENTA
class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            'fecha_venta': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }


class VentaUpadteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            'fecha_venta': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }


# DETALLE VENTA
class Detalle_ventaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_venta
        fields = "__all__"


class Detalle_ventaUpadteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_venta
        fields = "__all__"


# RESERVA
class ReservaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Reserva
        fields = "__all__"
        widgets = {
            'fecha_reserva': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'hora_inicio': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'hora_fin': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_abono': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_pago_total': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class ReservaUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Reserva
        fields = "__all__"
        widgets = {
            'fecha_reserva': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'hora_inicio': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'hora_fin': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'fecha_abono': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_pago_total': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


# UBICACION
class UbicacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Ubicacion
        fields = "__all__"
        exclude = ["estado", ]


class UbicacionUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Ubicacion
        fields = "__all__"
        exclude = ["estado", ]
