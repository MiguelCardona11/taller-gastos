from enums import MetodoPago, TipoGasto

class Gasto:
    def __init__(self, valor_gastado:float, metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        self._valor_gastado = valor_gastado
        self._metodo_pago = metodo_pago
        self._tipo_gasto = tipo_gasto
