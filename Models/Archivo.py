import os

class Archivo:
    def __init__(self, nombre_archivo, ruta):
        if not nombre_archivo.endswith('.txt'):
            nombre_archivo += '.txt'
        self._nombre_archivo = nombre_archivo
        self._ruta = ruta
        self._contenido = str
    
    """
    Método que se encarga de crear el archivo si no existe y de
    escribirle dentro el texto indicado.
    :param contenido: cadena de texto a escribir en el archivo.
    """
    def llenar_archivo(self, contenido) -> None:
        ruta_completa = os.path.join(self._ruta, self._nombre_archivo)
        
        if not os.path.exists(self._ruta):
            os.makedirs(self._ruta)
        
        with open(ruta_completa, 'a') as archivo:
            archivo.write(contenido + '\n')
        
    """
    Método que vacía todo el contenido del archivo de texto.
    """
    def vaciar_archivo(self) -> None:
        ruta_completa = os.path.join(self._ruta, self._nombre_archivo)
        
        with open(ruta_completa, 'w') as archivo:
            pass
    
    """
    Método que devuelve la ruta completa de un archivo.
    :return: cadena de texto con ruta completa.
    """
    def obtener_ruta_completa(self):
        return str(self._ruta)+"/"+str(self._nombre_archivo)