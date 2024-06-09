from datetime import date
from enums import Destino, MetodoPago, TipoGasto
from Models.Viaje import Viaje
from Controllers.ControlViaje import ControlViaje

def seleccionar_destino() -> str:
    """
    Método que muestra los destinos disponibles a partir de un Enum
    y permite seleccionar uno de ellos.
    :return: cadena correspondiente al destino seleccionado
    """
    print("\nSeleccione el destino:")
    for i, destino in enumerate(Destino, start=1):
        print(f"{i}. {destino.value}")
        
    while True:
        try:
            opcion = int(input("Seleccione el número correspondiente al destino: "))
            if 1 <= opcion <= len(Destino):
                return list(Destino)[opcion - 1].value
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            pass
        
def seleccionar_metodo_pago() -> str:
    """
    Método que muestra los métodos de pago disponibles a partir de un Enum
    y permite seleccionar uno de ellos.
    :return: cadena correspondiente al método de pago seleccionado
    """
    print("\nSeleccione el método de pago:")
    for i, metodo in enumerate(MetodoPago, start=1):
        print(f"{i}. {metodo.value}")
        
    while True:
        try:
            opcion = int(input("Seleccione el número correspondiente al método: "))
            if 1 <= opcion <= len(MetodoPago):
                return list(MetodoPago)[opcion - 1].value
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            pass

def seleccionar_tipo_gasto() -> str:
    """
    Método que muestra los tipos de gasto disponibles a partir de un Enum
    y permite seleccionar uno de ellos.
    :return: cadena correspondiente al tipo de gasto seleccionado
    """
    print("\nSeleccione el tipo de gasto:")
    for i, tipo in enumerate(TipoGasto, start=1):
        print(f"{i}. {tipo.value}")
        
    while True:
        try:
            opcion = int(input("Seleccione el número correspondiente al tipo de gasto: "))
            if 1 <= opcion <= len(TipoGasto):
                return list(TipoGasto)[opcion - 1].value
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            pass
       
def validar_fechas() -> date:
    """
    Método que valida que la fecha inicial ingresada no sea mayor a la final, y tenga formato correcto
    :return: valores de fecha de inicio y fecha de fin
    """   
    while True:
        try:
            fecha_inicio = date.fromisoformat(input("Ingrese la fecha de inicio (AAAA-MM-DD): "))
            fecha_final = date.fromisoformat(input("Ingrese la fecha final (AAAA-MM-DD): "))
            if fecha_inicio > fecha_final:
                print("La fecha de inicio no puede ser mayor que la fecha final. Intente nuevamente.")
            else:
                return fecha_inicio, fecha_final
        except ValueError:
            print("Formato de fecha inválido, Introduzca una fecha en formato AAAA-MM-DD.")
 
def validar_formato_fecha(mensaje) -> date:
    """
    Método que valida el formato de fecha ingresado (AAAA-MM-DD).
    :param mensaje: mensaje de input para pedir la fecha al usuario
    :return: valor de la fecha de tipom date
    """  
    while True:
        try:
            fecha = date.fromisoformat(input(mensaje))
            return fecha
        except ValueError:
            print("Formato de fecha inválido, Introduzca una fecha en formato AAAA-MM-DD.")
        
def seleccionar_fecha_dia(viaje: Viaje) -> date:
    """
    Método que verifica que una fecha indicada se encuentre dentro de las fechas de un viaje.
    correspondiente y que su formato sea correcto.
    :param viaje: viaje con una fecha inicial y final en donde se debe encontrar la fecha ingresada.
    :return: cadena correspondiente a la fecha escrita en formato date.
    """
    fin = True
    while fin:
        try:
            fecha_dia = date.fromisoformat(input("Ingrese la fecha del día a registrar el gasto (AAAA-MM-DD): "))
            if viaje._fecha_inicio <= fecha_dia <= viaje._fecha_final:
                fin = False
                return fecha_dia
            else:
                print("La fecha indicada no pertenece al viaje")
        except ValueError:
            print("Formato de fecha inválido, Introduzca una fecha en formato AAAA-MM-DD.")
        
def main():
    fin = False
    control_viaje = ControlViaje()

    while not fin:
        print("¡Bienvenido!, para iniciar por favor registre su viaje")
        
        # Creación de viaje
        destino = seleccionar_destino()
        presupuesto = float(input("Ingrese el presupuesto diario estimado: "))
        fecha_inicio, fecha_final = validar_fechas()
        viaje = Viaje(destino, presupuesto, fecha_inicio, fecha_final)
        
        viaje.agregar_dias_viaje()
        
        # Agregar gastos a un día
        agregar_gastos = input("\n¿Desea agregar gastos a un día? (s/n): ").lower()
        while agregar_gastos == 's':
            fecha_dia = seleccionar_fecha_dia(viaje)
            valor_gastado = float(input("Ingrese el valor gastado: "))
            metodo_pago = seleccionar_metodo_pago()
            tipo_gasto = seleccionar_tipo_gasto()
            
            diferencia = control_viaje.registrar_gasto(viaje, fecha_dia, valor_gastado, metodo_pago, tipo_gasto)
            print("\n--> Diferencia de gasto con respecto al presupuesto diario: " + diferencia)
            
            agregar_gastos = input("\n¿Desea agregar otro gasto a un día? (s/n): ").lower()
                    
        ruta = control_viaje.reporte_gasto_diario_por_tipo_metodo(viaje)
        print("Reporte creado con éxito en "+ruta)
        
        # Preguntar si desea registrar un nuevo viaje
        nuevo_viaje = input("\n¿Desea registrar un nuevo viaje? (s/n): ").lower()
        if nuevo_viaje == 'n':
            fin = True

if __name__ == "__main__":
    main()