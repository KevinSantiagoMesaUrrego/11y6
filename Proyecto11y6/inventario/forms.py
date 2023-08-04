from django import forms
from django.forms import ModelForm
from inventario.models import Producto, Marca, Presentacion, UnidadMedida, ConsumoTrabajador


# PRODUCTO

class Productoform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Producto
        fields = "__all__"
        exclude = ('estado',)


class ProductoUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Producto
        fields = "__all__"
        exclude = ('estado',)


# MARCA

class Marcaform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Marca
        fields = "__all__"
        exclude = ('estado',)


class MarcaUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Marca
        fields = "__all__"
        exclude = ('estado',)


# PRESENTACION

class Presentacionform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Presentacion
        fields = "__all__"
        exclude = ('estado',)


class PresentacionUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = Presentacion
        fields = "__all__"
        exclude = ('estado',)


# UNIDADMEDIDA

class UnidadMedidaform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = UnidadMedida
        fields = "__all__"
        exclude = ('estado',)


class UnidadMedidaUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = UnidadMedida
        fields = "__all__"
        exclude = ('estado',)


# CONSUMOTRABJADOR

class ConsumoTrabjadorform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = ConsumoTrabajador
        fields = "__all__"


class ConsumoTrabajadorUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control small-input'

    class Meta:
        model = ConsumoTrabajador
        fields = "__all__"
