from enums import *
from Models.Viaje import *
from Models.DiasViaje import *
from Models.Gasto import *
from Controllers.ControlViaje import *
from datetime import date


"""
Método que muestra los destinos disponibles a partir de un Enum
y permite seleccionar uno de ellos.
:return: cadena correspondiente al destino seleccionado
"""
def seleccionar_destino() -> str:
    print("Seleccione el destino:")
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
        
"""
Método que muestra los métodos de pago disponibles a partir de un Enum
y permite seleccionar uno de ellos.
:return: cadena correspondiente al método de pago seleccionado
"""
def seleccionar_metodo_pago() -> str:
    print("Seleccione el método de pago:")
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
        
"""
Método que muestra los tipos de gasto disponibles a partir de un Enum
y permite seleccionar uno de ellos.
:return: cadena correspondiente al tipo de gasto seleccionado
"""
def seleccionar_tipo_gasto() -> str:
    print("Seleccione el tipo de gasto:")
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
        

"""
Método que valida que la fecha inicial ingresada no sea mayor a la final, y tenga formato correcto
:return: valores de fecha de inicio y fecha de fin
"""          
def validar_fechas() -> date:
    while True:
        try:
            fecha_inicio = date.fromisoformat(input("Ingrese la fecha de inicio (AAAA-MM-DD): "))
            fecha_final = date.fromisoformat(input("Ingrese la fecha final (AAAA-MM-DD): "))
            if fecha_inicio > fecha_final:
                print("La fecha de inicio no puede ser mayor que la fecha final. Intente nuevamente.")
            else:
                return fecha_inicio, fecha_final
        except ValueError:
            pass

"""
Método que valida el formato de fecha ingresado (AAAA-MM-DD).
:param mensaje: mensaje de input para pedir la fecha al usuario
:return: valor de la fecha de tipom date
"""   
def validar_formato_fecha(mensaje) -> date:
    while True:
        try:
            fecha = date.fromisoformat(input(mensaje))
            return fecha
        except ValueError:
            pass
        

def seleccionar_fecha_dia(viaje: Viaje):
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
            print("Ingrese una fecha válida en el formato AAAA-MM-DD")

    
        
        
def main():
    fin = False

    while not fin:
        # Creación de viaje
        destino = seleccionar_destino()
        presupuesto = float(input("Ingrese el presupuesto estimado: "))
        fecha_inicio, fecha_final = validar_fechas()
        viaje = Viaje(destino, presupuesto, fecha_inicio, fecha_final)
        
        viaje.agregar_dias_viaje()
        
        # Agregar gastos a un día
        agregar_gastos = input("¿Desea agregar gastos a un día? (s/n): ").lower()
        if agregar_gastos == 's':
            while True:
                
                fecha_dia = seleccionar_fecha_dia(viaje)
                valor_gastado = float(input("Ingrese el valor gastado: "))
                metodo_pago = seleccionar_metodo_pago()
                tipo_gasto = seleccionar_tipo_gasto()
                
                ControlViaje.registrar_gasto()
                    

                    
                gasto = Gasto(valor_gastado, metodo_pago, tipo_gasto)
                dia_viaje.agregar_gasto(gasto)
                    
                agregar_gastos = input("¿Desea agregar otro gasto a este día? (s/n): ").lower()
                
                viaje.agregar_dia(dia_viaje)
                
                agregar_otro_gasto = input("¿Desea agregar otro gasto al viaje? (s/n): ").lower()
                if agregar_otro_gasto != 's':
                    break
    
        fin = True

if __name__ == "__main__":
    main()
    
    