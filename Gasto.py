from enums import MetodoPago, TipoGasto

class Gasto:
    def __init__(self, valor_gastado:float, metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        self._valor_gastado = valor_gastado
        self._metodo_pago = metodo_pago
        self._tipo_gasto = tipo_gasto
    
    def calcular_consumo(self, area:float, tipo:str) -> float:
        """
        lorem ipsum
        :param X:
        :return:
        """
        
        if area >= 0:
            if tipo == 't':
                return 0.5 * area
            elif tipo == 'h':
                return 0.25 * area
            else:
                raise ValueError("Formato de tipo incorrecto, debe ser 'h' o 't'")
        else:
            raise ValueError("El area no puede ser negativa")
        