from django.db import models

# Create your models here.

class Persona:
    idPersona:int
    nombrePersona:str
    apellidoPersona:str
    tipoDocumentacionPersona:str
    rolPersona:str
    direccionPersona:str
    correoPersona:str
    usuarioPersona:str
    contraseñaPersona:str
    valorTotalSalarioPersona:float
    funcionPersona:str
    estadoPersona:Tinyint
    Turno_idTurno:int
    Eps_idEps:int



class Eps:
    idEps:int
    nombreEps:str
    estadoEps:Tinyint


class Trabajador:
    N°DocumentoTrabajador:int
    nombreTrabajador:str
    apellidoTrabajador:str
    telefonoTrabajador:str
    correoTrabajador:str
    direccionTrabajador:str
    usuarioTrabajadro:str
    contraseñaTrabajadro:str
    Eps_idEps:int
    Turno_idTurno:int


class Turno:
    idTurno:int
    horaIngresoTurno:date
    horaSalidaTurno:date
    estadoTurno:Tinyint


    
