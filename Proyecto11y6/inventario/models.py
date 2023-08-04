from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.models import Trabajador




# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Marca")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)


class Presentacion(models.Model):
    presentacion = models.CharField(max_length=45, verbose_name="Presentacion")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)


class UnidadMedida(models.Model):
    unidadmedida = models.CharField(max_length=45, verbose_name="Medida")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)




class Producto(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre")
    descripcion = models.CharField(max_length=45, verbose_name="Descripcion")
    precio = models.FloatField(verbose_name="Precio")
    oferta = models.IntegerField(verbose_name="Oferta")
    stock = models.IntegerField(verbose_name="Stock")
    marca_producto = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    presentacion_producto = models.ForeignKey(Presentacion, on_delete=models.CASCADE, verbose_name="Presentacion")
    medida_producto = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, verbose_name="Unidad Medida")

    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)

    def __str__(self):
        return "%s " % (self.nombre)



class ConsumoTrabajador(models.Model):
    from venta.models import Detalle_venta
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, verbose_name="Nombre Trabajador")
    nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    detalle_venta = models.ForeignKey(Detalle_venta, on_delete=models.CASCADE, verbose_name="Detalle")
    class Meta:
        verbose_name_plural = "Consumostrabajadores"