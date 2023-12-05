from django import forms
from django.forms import ModelForm, widgets
from compra.models import Compra, Detalle_compra, Evento, Proveedor


class CompraForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Compra
        fields = "__all__"
        widgets = {
            'fecha_compra': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
        exclude = ["estado",]


class CompraUpdateForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Compra
        fields = "__all__"
        exclude = ["estado",]


class Detalle_compraForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_compra
        fields = "__all__"
        exclude = ["estado"]


class Detalle_compraUpdateForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_compra
        fields = "__all__"


class EventoForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Evento
        fields = "__all__"
        widgets = {
            'fecha_inicio': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
        exclude = ('estado_evento',)


class EventoUpdateForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Evento
        fields = "__all__"
        exclude = ('estado_evento',)


class ProveedorForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Proveedor
        fields = "__all__"
        exclude = ["estado_proveedor", ]


class ProveedorUpdateForm(ModelForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Proveedor
        fields = "__all__"
        exclude = [" tipo_identificacion", "estado_proveedor"]