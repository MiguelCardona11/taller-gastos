from DiasViaje import DiasViaje
from datetime import date
from typing import List
from enums import Destino

class Viaje:
    def __init__(self, lugar_destino: Destino, presupuesto_estimado: float, fecha_inicio: date, fecha_final: date):
        self._lugar_destino = lugar_destino
        self._presupuesto_estimado = presupuesto_estimado
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self._DiasViaje: List[DiasViaje] = []
        
    def agregar_dia(self, dia_viaje: DiasViaje):
        self._DiasViaje.append(dia_viaje)

    def obtener_dia(self) -> List[DiasViaje]:
        return self._DiasViaje