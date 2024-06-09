import unittest
from enums import Destino, MetodoPago, TipoGasto
from Controllers.ControlViaje import ControlViaje
from Models.Viaje import Viaje
from Models.DiasViaje import DiasViaje

class test_viaje(unittest.TestCase):
    def test_registrar_gasto_diferencia_negativa(self):
        viaje = Viaje(Destino.USA, 1000, "2024-06-10", "2024-06-20")
        dia = DiasViaje("2024-06-10")
        viaje.agregar_dia(dia)
        control_viaje = ControlViaje()
        diferencia = control_viaje.registrar_gasto(viaje, "2024-06-10", 1500, MetodoPago.EFECTIVO, TipoGasto.ENTRETENIMIENTO)
        self.assertEqual("negativa", diferencia)
    
    def test_registrar_gasto_diferencia_positiva(self):
        viaje = Viaje(Destino.USA, 1000, "2024-06-10", "2024-06-20")
        dia = DiasViaje("2024-06-10")
        viaje.agregar_dia(dia)
        control_viaje = ControlViaje()
        diferencia = control_viaje.registrar_gasto(viaje, "2024-06-10", 200, MetodoPago.EFECTIVO, TipoGasto.ENTRETENIMIENTO)
        self.assertEqual("positiva", diferencia)
        
    def test_registrar_gasto_diferencia_cero(self):
        viaje = Viaje(Destino.USA, 1000, "2024-06-10", "2024-06-20")
        dia = DiasViaje("2024-06-10")
        viaje.agregar_dia(dia)
        control_viaje = ControlViaje()
        diferencia = control_viaje.registrar_gasto(viaje, "2024-06-10", 1000, MetodoPago.EFECTIVO, TipoGasto.ENTRETENIMIENTO)
        self.assertEqual("cero", diferencia)