from django.db import models
from django.utils.translation import gettext_lazy as _
from usuario.models import Trabajador
from venta.models import Venta

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Producto")
    descripcion=models.CharField(max_length=45,verbose_name="Descripcion")
    precio=models.FloatField(verbose_name="Precio")
    oferta=models.IntegerField(verbose_name="Oferta")
    stock=models.IntegerField(verbose_name="Stock")
    class Estado(models.TextChoices):
            ACTIVO='1',_("Activo")
            INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,verbose_name="Estado",default=Estado.ACTIVO)
    def __str__(self):
        return "%s "%(self.nombre)

    #id automaticas
    # Marca_idMarca:int
    # Presentacion_idPresentacion:int
    # UnidadMedida_idUnidadMedida:int
    # Venta_idVenta:int



class Marca(models.Model):
    #Automatico
    #idMarca:int
    nombre=models.CharField(max_length=45,verbose_name="Marca")
    class Estado(models.TextChoices):
            ACTIVO='1',_("Activo")
            INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,verbose_name="Estado",default=Estado.ACTIVO)


class Presentacion(models.Model):
    #Automatico
    #idPresentacion:int
    presentacion=models.CharField(max_length=45,verbose_name="Presentacion")
    class Estado(models.TextChoices):
            ACTIVO='1',_("Activo")
            INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,verbose_name="Estado",default=Estado.ACTIVO)


class UnidadMedida(models.Model):
    #Automatico
    #idUnidadMedida:int
    unidadmedida=models.CharField(max_length=45,verbose_name="Medida")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,verbose_name="Estado",default=Estado.ACTIVO)


class ConsumoTrabajador(models.Model):
    #Automatico
    #idConsumoTrabajador:int
    #Producto_idProducto:int
    trabajador=models.ForeignKey(Trabajador, on_delete=models.CASCADE,verbose_name="Nombre Trabajador")

    class Meta:
        verbose_name_plural = "Consumostrabajadores"



