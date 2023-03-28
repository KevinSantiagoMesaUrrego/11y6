from django.db import models

# Create your models here.

class Detalle_Compra:
    idDetalleCompra:int
    CantidadProducto:int
    valorTotalDetalleCompra:float
    producto_idProducto:int


class Proveedor:
    idProveedor:int
    tipoIdentificacionProveedor:str
    nombreProveedor:str
    telefonoProveedor:str
    correoProveedor:str
    direccionProveedor:str
    estadoProveedor:str


class Compra:
    idCompra:int
    fechaCompra:datetime
    DetalleCompra_idDetalleCompra:int
    Proveedor_idProveedor:int
    Persona_idPersona:int


class Evento:
    idEvento:int
    nombreEvento:str
    fechaInicioEvento:datetime
    fechaFiinalEvento:datetime
    descripcionEvento:longtext
    estadoEvento:Tinyint
    Compra_idCompra:int






