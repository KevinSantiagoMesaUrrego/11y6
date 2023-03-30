from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Compra(models.Model):
       fecha_compra= models.DateField(verbose_name="Fecha Compra", help_text="MM/DD/AAAA")
      
class Detalle_compra(models.Model):
        cantidad_producto=models.IntegerField(max_length=45,verbose_name="Cantidad Producto")
        valor_total=models.FloatField(max_length=45,verbose_name="Valor Total Compra")

class Proveedor(models.Model):
    class Tipo_identificacion(models.TextChoices):
            CEDULA='CC',_("Cédula")
            CEDULA_EXTRANJERIA='CE',_("Cédula de Extranjería")
    tipo_identificacion=models.CharField(max_length=2,choices=Tipo_identificacion.choices,verbose_name="Tipo de Identificación")
    nombre_proveedor= models.CharField(max_length=45,verbose_name="Nombre Proveedor")
    apellido_proveedor= models.CharField(max_length=45,verbose_name="Apellido Proveedor")
    telefono=models.CharField(max_length=10,verbose_name="Teléfono")
    correo_proveedor= models.CharField(max_length=50,verbose_name="Correo Proveedor")
    direccion_proveedor= models.CharField(max_length=50,verbose_name="Dirección Proveedor")
    class Estado_proveedor(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado_proveedor=models.CharField(max_length=1,choices=Estado_proveedor.choices,default=Estado_proveedor.ACTIVO,verbose_name="Estado Proveedor")

    def clean(self):
            self.nombre_proveedor= self.nombre_proveedor.title()
            self.apellido_proveedor= self.apellido_proveedor.title()
            self.correo_proveedor= self.correo_proveedor.lower()
    def __str__(self):
            return "%s %s"%(self.nombre_proveedor,self.apellido_proveedor)

class Evento(models.Model):
    nombre_evento= models.CharField(max_length=45,verbose_name="Nombre Evento") 
    fecha_inicio= models.DateField(verbose_name="Fecha Incio Evento", help_text="MM/DD/AAAA")
    fecha_fin= models.DateField(verbose_name="Fecha Fin Evento", help_text="MM/DD/AAAA")
    descripcion= models.CharField(max_length=200,verbose_name="Descripción Evento")
    class Estado_evento(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado_evento=models.CharField(max_length=1,choices=Estado_evento.choices,default=Estado_evento.ACTIVO,verbose_name="Estado Evento")





