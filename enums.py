from enum import Enum

class Destino(Enum):
    COLOMBIA = "COLOMBIA"
    USA = "USA"
    EUROPA = "EUROPA"
    
class MetodoPago(Enum):
    EFECTIVO = "EFECTIVO"
    TARJETA = "TARJETA"
    
class TipoGasto(Enum):
    TRANSPORTE = "TRANSPORTE"
    ALOJAMIENTO = "ALOJAMIENTO"
    ALIMENTACION = "ALIMENTACION"
    ENTRETENIMIENTO = "ENTRETENIMIENTO"
    COMPRAS = "COMPRAS"