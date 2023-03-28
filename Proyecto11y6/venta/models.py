from django.db import models

# Create your models here.

class Reserva:
    idReserva:int
    fechaReserva:date
    horaInicioReserva:date
    horaFinReserva:date
    costoReserva:float
    abonoReserva:float
    fechaAbonoReserva:date
    pagoTotalReserva:float
    fechaPagoTotalReserva:date
    Ubicacion_idUbicacion:int
    Persona_idPersona:int


class Ubicacion:
    idUbicacion:int
    nombreUbicacion:str
    estadoUbicacion:Tinyint


class DetalleVenta:
    idDetalleVenta:int
    cantidadProducto:int
    Reserva_idReserva:int
    Trabajador_N°DocumentoTrabajador:int


class Venta:
    idVenta:int
    fechaVenta:date 
    DetalleVenta_idDetalleVenta:int

    
