from django import forms
from django.forms import ModelForm, widgets
from compra.models import Compra, Detalle_compra, Evento, Proveedor


class CompraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Compra
        fields = "__all__"
        widgets = {
            'fecha_compra': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }


class CompraUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Compra
        fields = "__all__"


class Detalle_compraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_compra
        fields = "__all__"


class Detalle_compraUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Detalle_compra
        fields = "__all__"


class EventoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Evento
        fields = "__all__"
        exclude = ('estado_evento',)


class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Proveedor
        fields = "__all__"
        exclude = ["estado_proveedor", ]


class ProveedorUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Proveedor
        fields = "__all__"
        exclude = [" tipo_identificacion", "estado_proveedor"]
