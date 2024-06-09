from Models.Viaje import *
from Models.DiasViaje import *
from Models.Gasto import *
from enums import *

class ControlViaje:
    
    """
    Método que busca un objeto de tipo DiasViaje según su fecha.
    :param viaje: Viaje al que pertenece el DiaViaje buscado.
    :param fecha: Fecha perteneciente al DiaViaje buscado.
    :return: objeto de tipo DiasViaje.
    """
    def buscar_dia(self, viaje: Viaje, fecha: date) -> DiasViaje:
        for dia in viaje._DiasViaje:
            if fecha == dia._fecha:
                return dia
    
    """
    Método que guarda un gasto en la lista de gastos de un DiaViaje.
    :param dia: objeto de tipo DiasViaje.
    :param gasto: objeto de tipo Gasto a guardar.
    """
    def guardar_gasto(self, dia: DiasViaje, gasto: Gasto) -> None:
        dia.agregar_gasto(gasto)
        
    """
    Método que registra un gasto dentro de la lista de gastos de un día de viaje
    e indica la diferencia de presupuesto diario.
    :param viaje: Viaje al que pertenece dicho gasto.
    :param fecha_dia: día en el que se registrarpa el gasto.
    :param valor_gastado: cantidad de dinero gastada.
    :param metodo_pago: método de pago del gasto.
    :param tipo_gasto: tipo de gasto realizado.
    :return: diferencia del gasto con respecto a presupuesto diario
    """
    def registrar_gasto(self, viaje: Viaje, fecha_dia: date, valor_gastado: float, metodo_pago: MetodoPago, tipo_gasto: TipoGasto) -> str:
        dia = self.buscar_dia(viaje, fecha_dia)
        gasto = Gasto(valor_gastado, metodo_pago, tipo_gasto)
        self.guardar_gasto(dia, gasto)
        
        if valor_gastado > viaje.obtener_presupuesto():
            diferencia = "negativa"
        elif valor_gastado < viaje.obtener_presupuesto():
            diferencia = "positiva"
        else:
            diferencia = "cero"
        return diferencia
    