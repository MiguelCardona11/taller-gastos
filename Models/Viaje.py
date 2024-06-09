from Models.DiasViaje import DiasViaje
from datetime import date, timedelta
from typing import List
from enums import Destino

class Viaje:
    def __init__(self, lugar_destino: Destino, presupuesto_estimado: float, fecha_inicio: date, fecha_final: date):
        self._lugar_destino = lugar_destino
        self._presupuesto_estimado = presupuesto_estimado
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final
        self._DiasViaje: List[DiasViaje] = []

    def obtener_dias_viaje(self) -> List[DiasViaje]:
        return self._DiasViaje
    
    """
    Método que crea objetos de tipo DiasViaje a partir
    de las fechas de inicio y fin de un viaje.
    :return: Retorna True si la creación es exitosa.
    """
    def agregar_dias_viaje(self) -> bool:
        dia_actual = self._fecha_inicio
        while dia_actual <= self._fecha_final:
            nuevo_dia_viaje = DiasViaje(dia_actual)
            self._DiasViaje.append(nuevo_dia_viaje)
            dia_actual += timedelta(days=1)
        return True
    
    """
    Método que imprime todas las fechas de un viaje.
    """
    def imprimir_fechas_viaje(self):
        for dia in self._DiasViaje:
            print(dia.obtener_fecha())
            
    def obtener_presupuesto(self):
        return self._presupuesto_estimado
    

    
    
