from django.db import models
from django.utils.translation import gettext_lazy as _

#Create your models here.

class Persona(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombres Completo:")
    apellido= models.CharField(max_length=45,verbose_name="Apellidos Completos:")
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento:")
    documento=models.PositiveIntegerField(verbose_name="Documento:")
    class Rol(models.TextChoices):
        INSTRUCTOR='E',_("Empleado")
        APRENDIZ='A',_("Administrador")
    rol=models.CharField(max_length=1,choices=Rol.choices,verbose_name="Rol:")
    direccion=models.CharField(max_length=45,verbose_name="Dirección:")
    correo=models.CharField(max_length=45,verbose_name="Correo electronico:")
    usuario=models.CharField(max_length=45,verbose_name="Usuario:")
    contrasena=models.CharField(max_length=45,verbose_name="Contraseña:")
    salario=models.CharField(max_length=45,verbose_name="Salario:")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    def clean(self):
        self.nombre= self.nombre.title()
        self.apellido= self.apellido.title()
        self.correo= self.correo.lower()
    def __str__(self):
        return "%s %s"%(self.nombre,self.apellido)
    class Meta:
        verbose_name_plural = "Personas"



class Eps(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Nombre EPS:")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")


class Trabajador(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre:")
    apellido= models.CharField(max_length=45,verbose_name="Apellido:")
    documento=models.IntegerField(max_length=10,verbose_name="Documento:")
    telefono=models.CharField(max_length=10,verbose_name="Telefono")
    correo=models.CharField(max_length=45,verbose_name="Correo electronico:")
    direccion=models.CharField(max_length=45,verbose_name="Dirección:")
    usuario=models.CharField(max_length=45,verbose_name="Usuario:")
    contrasena=models.CharField(max_length=45,verbose_name="Contraseña:")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")


class Turno(models.Model):
    fecha_ingreso= models.DateTimeField(verbose_name="Fecha de Ingreso", help_text="HH/MM/SS")
    fecha_salida= models.DateTimeField(verbose_name="Fecha de Salida", help_text="HH/MM/SS")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")



