from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Producto(models.Model):
    nombreProducto=models.CharField(max_length=45,verbose_name="Producto")
    descripcionProducto=models.CharField(max_length=45,verbose_name="Descripcion")
    precioProducto=models.FloatField(max_length=45,verbose_name="Precio")
    ofertaProducto=models.IntegerField(max_length=45,verbose_name="Oferta")
    stockProducto=models.IntegerField(max_length=45,verbose_name="Stock")
    class Estado_producto(models.TextChoices):
            ACTIVO='A',_("Activo")
            INACTIVO='I',_("Inactivo")
    #id automaticas
    # Marca_idMarca:int
    # Presentacion_idPresentacion:int
    # UnidadMedida_idUnidadMedida:int
    # Venta_idVenta:int



class Marca(models.Model):
    #Automatico
    #idMarca:int
    nombreMarca=models.CharField(max_length=45,verbose_name="Marca")
class estadoMarca(models.TextChoices):
    ACTIVO='A',_("Activo")
    INACTIVO='I',_("Inactivo")


class Presentacion(models.Model):
    #Automatico
    #idPresentacion:int
    
    nombrePresentacion=models.CharField(max_length=45,verbose_name="Presentacion")
class estadoPresentacion(models.TextChoices):
    ACTIVO='A',_("Activo")
    INACTIVO='I',_("Inactivo")
    


class UnidadMedida(models.Model):
    #Automatico
    #idUnidadMedida:int
    nombreUnidadMedida=models.CharField(max_length=45,verbose_name="Medida")
class estadoUnidadMedida(models.TextChoices):
    ACTIVO='A',_("Activo")
    INACTIVO='I',_("Inactivo")


class ConsumoTrabajador(models.Model):
    #Automatico
    #idConsumoTrabajador:int
    #Producto_idProducto:int
    
    Trabajador_NDocumentoTrabajador=models.IntegerField(max_length=45,verbose_name="Documento")


