from Gasto import Gasto
from datetime import date
from typing import List

class DiasViaje:
    def __init__(self, fecha: date):
        self._fecha = fecha
        self._gastos: List[Gasto] = []
        
    def agregar_gasto(self, gasto: Gasto):
        self._gastos.append(gasto)

    def obtener_gastos(self) -> List[Gasto]:
        return self._gastos