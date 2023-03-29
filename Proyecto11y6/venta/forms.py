from django import forms
from django.forms import ModelForm,widgets
from venta.models import Venta,Detalle_venta,Reserva,Ubicacion
#VENTA
class VentaForm(ModelForm):
    class Meta:
        model=Venta
        fields="__all__"
        widgets={
            'fecha_venta': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class VentaUpadteForm(ModelForm):
    class Meta:
        model=Venta
        fields="__all__"
#DETALLE VENTA
class Detalle_ventaForm(ModelForm):
    class Meta:
        model=Detalle_venta
        fields="__all__"

class Detalle_ventaUpadteForm(ModelForm):
    class Meta:
        model=Detalle_venta
        fields="__all__"
#RESERVA
class ReservaForm(ModelForm):
    class Meta:
        model=Reserva
        fields="__all__"

class ReservaUpdateForm(ModelForm):
    class Meta:
        model=Reserva
        fields="__all__"
#UBICACION
class UbicacionForm(ModelForm):
    class Meta:
        model=Ubicacion
        fields="__all__"

class UbicacionUpdateForm(ModelForm):
    class Meta:
        model=Ubicacion
        fields="__all__"