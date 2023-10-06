from django.db import models
from django.utils.translation import gettext_lazy as _
from inventario.models import Producto
from safedelete.models import SafeDeleteModel
# Create your models here.
class Venta(SafeDeleteModel):
    fecha_venta = models.DateField(verbose_name="fecha venta", help_text="MM/DD/AAAA", auto_now_add=True)
    numero_mesa = models.IntegerField(verbose_name="numero de mesa")
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)

class Detalle_venta(SafeDeleteModel):
    venta= models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="producto")
    cantidad_producto = models.IntegerField(verbose_name="Cantidad Producto")


    def _str_(self):
        return " %s %s" % (self.cantidad_producto, self.valor_total)


class Ubicacion(SafeDeleteModel):
    nombre = models.CharField(max_length=45, verbose_name="Nombre")
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO)
    def _str_(self):
        return "%s " % (self.nombre)
class Reserva(SafeDeleteModel):
    ubicacion_nombre = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, verbose_name="ubicación nombre")
    cliente= models.CharField(max_length=45, verbose_name="nombre cliente")
    def _str_(self):
        return "%s " % (self.ubicacion_nombre)