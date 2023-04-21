from django import forms
from django.forms import ModelForm
from inventario.models import Producto,Marca,Presentacion,UnidadMedida,ConsumoTrabajador

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

class UnidadMedidaform(ModelForm):
    class Meta:
        model=UnidadMedida
        fields="__all__"

class UnidadMedidaUpdateForm(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"

#CONSUMOTRABJADOR

class ConsumoTrabjadorform(ModelForm):
    class Meta:
        model=ConsumoTrabajador
        fields="__all__"

class ConsumoTrabajadorUpdateForm(ModelForm):
    class Meta:
        model=Producto
        fields="__all__"