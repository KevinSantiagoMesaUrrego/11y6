# models.py
from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel
class Register(SafeDeleteModel):
    correo = models.EmailField(max_length=45, verbose_name="Correo:")
    usuario = models.CharField(max_length=45, verbose_name="Usuario:")
    contraseña = models.CharField(max_length=45, verbose_name="Contraseña:")
    activo = models.BooleanField(default=False)
    def clean(self):
        self.correo = self.correo.title()
        self.usuario = self.usuario.title()
        self.contraseña = self.contraseña.lower()

    def __str__(self):
        return "%s %s" % (self.correo, self.usuario)

    class Meta:
        verbose_name_plural = "Registers"
