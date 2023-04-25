from django import forms
from django.forms import ModelForm
from inventario.models import Producto,Marca,Presentacion,Unidad_medida,Consumo_trabajador

#PRODUCTO

class Productoform(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"

class ProductoUpdateForm(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"

#MARCA

class Marcaform(ModelForm):
    class Meta:
        model=Marca
        fields="__all__"

class MarcaUpdateForm(ModelForm):
    class Meta:
        model=Marca
        fields="__all__"

#PRESENTACION

class Presentacionform(ModelForm):
    class Meta:
        model=Presentacion
        fields="__all__"

class PresentacionUpdateForm(ModelForm):
    class Meta:
        model=Presentacion
        fields="__all__"

#UNIDADMEDIDA

class Unidad_medidaform(ModelForm):
    class Meta:
        model=Unidad_medida
        fields="__all__"

class Unidad_medidaUpdateForm(ModelForm):
    class Meta:
        model=Unidad_medida
        fields="__all__"

#CONSUMOTRABJADOR

class Consumo_trabjadorform(ModelForm):
    class Meta:
        model=Consumo_trabajador
        fields="__all__"

class Consumo_trabajadorUpdateForm(ModelForm):
    class Meta:
        model=Consumo_trabajador
        fields="__all__"