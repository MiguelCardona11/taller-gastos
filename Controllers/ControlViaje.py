from Models.Viaje import *
from Models.DiasViaje import *
from Models.Gasto import *
from enums import *
import requests

class ControlViaje:
    
    """
    Método que busca un objeto de tipo DiasViaje según su fecha.
    :param viaje: Viaje al que pertenece el DiaViaje buscado.
    :param fecha: Fecha perteneciente al DiaViaje buscado.
    :return: objeto de tipo DiasViaje.
    """
    def buscar_dia(self, viaje: Viaje, fecha: date) -> DiasViaje:
        for dia in viaje.obtener_dias_viaje():
            if fecha == dia.obtener_fecha():
                return dia
        return None
    
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
    
    def uso_api(self):
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        data = response.json()
        random_number = data[0]['random']
        return random_number
    
    def reporte_gasto_diario_por_tipo_metodo(self, viaje: Viaje):
        cambio = 1
        if viaje._lugar_destino == "USA":
            cambio = self.uso_api()
        elif viaje._lugar_destino == "EUROPA":
            cambio = self.uso_api() + 200
        
        for dia in viaje.obtener_dias_viaje():
            gasto_efectivo = 0
            gasto_tarjeta = 0
            gasto_diario_total = 0
            for gasto in dia.obtener_gastos():
                gasto_efectivo = 0
                gasto_tarjeta = 0
                gasto_diario_total = 0
                if gasto._metodo_pago == "EFECTIVO":
                    gasto_efectivo += gasto.obtener_valor_gastado()
                    gasto_efectivo = gasto_efectivo*cambio
                elif gasto._metodo_pago == "TARJETA":
                    gasto_tarjeta += gasto.obtener_valor_gastado()
                    gasto_tarjeta = gasto_tarjeta*cambio
                gasto_diario_total = gasto_efectivo + gasto_tarjeta
            print("Gastos para el día "+str(dia._fecha)+" (COP): \nGasto en efectivo: "+str(gasto_efectivo)+"\nGasto en tarjeta: "+str(gasto_tarjeta)+"\nTotal: "+str(gasto_diario_total)+"\n")