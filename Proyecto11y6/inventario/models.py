from django.db import models

# Create your models here.

class Producto:
    idProducto:int
    nombreProducto:str
    descripcionProducto:str
    precioProducto:float
    tipoProducto:str
    ofertaProducto:int
    stockProducto:int
    estadoProducto:Tinyint
    Marca_idMarca:int
    Presentacion_idPresentacion:int
    UnidadMedida_idUnidadMedida:int
    Venta_idVenta:int



class Marca:
    idMarca:int
    nombreMarca:str
    estadoMarca:Tinyint


class Presentacion:
    idPresentacion:int
    nombrePresentacion:str
    estadoPresentacion:str


class UnidadMedida:
    idUnidadMedida:int
    nombreUnidadMedida:str
    estadoUnidadMedida:Tinyint


class ConsumoTrabajador:
    idConsumoTrabajador:int
    Producto_idProducto:int
    Trabajador_N°DocumentoTrabajador:int


