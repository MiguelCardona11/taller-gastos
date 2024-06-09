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
        return self._gastos
    
    def obtener_fecha(self):
        return self._fecha

    def imprimir_gastos_dia(self) -> None:
        """
        Método que imprime todos los gastos asociados a un DiaViaje
        """
        for gasto in self._gastos:
            print(gasto.obtener_valor_gastado())