from django.db import models
from django.utils.translation import gettext_lazy as _
from inventario.models import Producto
from safedelete.models import SafeDeleteModel

# Create your models here.

class Proveedor(SafeDeleteModel):
    class Tipo_identificacion(models.TextChoices):
        CEDULA = 'CC', _("Cédula")
        CEDULA_EXTRANJERIA = 'CE', _("Cédula de Extranjería")

    tipo_identificacion = models.CharField(max_length=2, choices=Tipo_identificacion.choices,
                                           verbose_name="Tipo de Identificación")
    nombre_proveedor = models.CharField(max_length=45, verbose_name="Nombre Proveedor")
    apellido_proveedor = models.CharField(max_length=45, verbose_name="Apellido Proveedor")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    correo_proveedor = models.CharField(max_length=50, verbose_name="Correo Proveedor")
    direccion_proveedor = models.CharField(max_length=50, verbose_name="Dirección Proveedor")

    class Estado_proveedor(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado_proveedor = models.CharField(max_length=1, choices=Estado_proveedor.choices, default=Estado_proveedor.ACTIVO,verbose_name="Estado Proveedor")

    def clean(self):
        self.nombre_proveedor = self.nombre_proveedor.title()
        self.apellido_proveedor = self.apellido_proveedor.title()
        self.correo_proveedor = self.correo_proveedor.lower()

    def _str_(self):
        return "%s %s" % (self.nombre_proveedor, self.apellido_proveedor)

    class Meta:
        verbose_name_plural = "Proveedores"


from django.db import models
from django.utils.translation import gettext as _
from safedelete.models import SafeDeleteModel


class Compra(SafeDeleteModel):
    fecha_compra = models.DateField(verbose_name="Fecha Compra", help_text="MM/DD/AAAA", auto_now_add=True)

    class Estado_compra(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado_compra = models.CharField(
        max_length=1,
        choices=Estado_compra.choices,
        default=Estado_compra.ACTIVO,
        verbose_name="Estado Evento"
    )

    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Nombre Proveedor" )
    def __str__(self):
        return "%s %s" % (self.id_proveedor, self.fecha_compra)

    class Meta:
        verbose_name_plural = "Compras"


class Detalle_compra(SafeDeleteModel):
    compra=models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="compra")
    cantidad_producto = models.IntegerField(verbose_name="Cantidad Producto")
    nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Nombre Producto")

    def _str_(self):
        return "%s %s" % (self.cantidad_producto)

    class Meta:
        verbose_name_plural = "detalles_compras"






class Evento(SafeDeleteModel):
    nombre_evento = models.CharField(max_length=45, verbose_name="Nombre Evento")
    fecha_inicio = models.DateField(verbose_name="Fecha Incio Evento", help_text="MM/DD/AAAA")
    fecha_fin = models.DateField(verbose_name="Fecha Fin Evento", help_text="MM/DD/AAAA")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción Evento")


    class Estado_evento(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")

    estado_evento = models.CharField(max_length=1, choices=Estado_evento.choices, default=Estado_evento.ACTIVO,
                                     verbose_name="Estado Evento")
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Fecha de Compra")

    def _str_(self):
        return "%s" % (self.id_compra)

class Personalizacion(SafeDeleteModel):
    nombre = models.CharField(max_length=45, verbose_name="Nombre")
    descripcion = models.CharField(max_length=45, verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA", auto_now=True)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True,default="productos/default-producto.png")
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO,
                                         verbose_name="Estado")
    def _str_(self):
        return "%s" % (self.nombre)