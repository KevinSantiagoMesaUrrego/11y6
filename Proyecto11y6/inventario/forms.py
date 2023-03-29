from django import forms

from django.forms import ModelForm, widgets
from inventario.models import Producto

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = "__all__"
        exclude=["stock",]
        # fields= ["Producto","Descripcion","Precio","Oferta"]
        
class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"
        

class Presentacion(ModelForm):
    
    class Meta:
        model = Presentacion
        fields = "__all__"
        # fields= ["Presentacion"]
      
class UnidadMedidaForm(ModelForm):
    class Meta:
        model = Medida
        fields = "__all__"
        exclude=["Medida"]

class ConsumoTrabajador(ModelForm):
    
    class Meta:
        model = Documento
        fields = "__all__"
        # fields= ["Documento"]
        


