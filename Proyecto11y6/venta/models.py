from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Venta (models.Model):
    fecha_venta=models.DateField(verbose_name="fecha venta",help_text="MM/DD/AAAA")

class Detalle_venta(models.Model):
    cantidad_producto=models.IntegerField(verbose_name="Cantidad Producto")
class Reserva(models.Model):
        fecha_reserva=models.DateField(verbose_name="Fecha Reserva",help_text="MM/DD/AAAA")
        hora_inicio=models.DateTimeField(verbose_name="Hora de Inicio",help_text="HH/MM/SS")
        hora_fin=models.DateTimeField(verbose_name="Hora de fin",help_text="HH/MM/SS")
        costo=models.FloatField()
        abono=models.FloatField()
        fecha_abono=models.DateField(verbose_name="Fecha Abono",help_text="MM/DD/AAAA")
        pago_total=models.FloatField()
        fecha_pago_total=models.DateField(verbose_name="Fecha Pago Total",help_text="MM/DD/AAAA")
class Ubicacion(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,verbose_name="Estado")

    
