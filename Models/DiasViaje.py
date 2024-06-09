from Models.Gasto import Gasto
from datetime import date
from typing import List

class DiasViaje:
    def __init__(self, fecha: date):
        self._fecha = fecha
        self._gastos: List[Gasto] = []
        
    def agregar_gasto(self, gasto: Gasto):
        self._gastos.append(gasto)

    def obtener_gastos(self):
        for gasto in self._gastos:
            print(gasto.obtener_valor_gastado())
    
    def obtener_fecha(self) -> date:
        return self._fecha
    
    

##

dia = DiasViaje("2024-03-20")