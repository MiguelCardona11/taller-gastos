import os

class Archivo:
    def __init__(self, nombre_archivo, ruta):
        if not nombre_archivo.endswith('.txt'):
            nombre_archivo += '.txt'
        self._nombre_archivo = nombre_archivo
        self._ruta = ruta
        self._contenido = str

    def llenar_archivo(self, contenido) -> None:
        """
        Método que se encarga de crear el archivo si no existe y de
        escribirle dentro el texto indicado.
        :param contenido: cadena de texto a escribir en el archivo.
        """
        ruta_completa = os.path.join(self._ruta, self._nombre_archivo)
        
        if not os.path.exists(self._ruta):
            os.makedirs(self._ruta)
        
        with open(ruta_completa, 'a', encoding="utf-8") as archivo:
            archivo.write(contenido + '\n')

    def vaciar_archivo(self) -> None:
        """
        Método que vacía todo el contenido del archivo de texto.
        """
        ruta_completa = os.path.join(self._ruta, self._nombre_archivo)
        
        with open(ruta_completa, 'w', encoding="utf-8") as archivo:
            pass

    def obtener_ruta_completa(self):
        """
        Método que devuelve la ruta completa de un archivo.
        :return: cadena de texto con ruta completa.
        """
        return str(self._ruta)+"/"+str(self._nombre_archivo)