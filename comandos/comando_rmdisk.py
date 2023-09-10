from .comando_base import Comando
import os

class Rmdisk(Comando):

    def __init__(self, parametros:dict) -> None:
        self.parametros = parametros

    def ejecutar(self):
        direccion = self.parametros.get("path")
        if direccion == None:
            print("Faltan parametros")
            return False
        if not os.path.isfile(direccion):
            print("La ruta no es un archivo valido")
            return False
        os.remove(direccion)
        print("El disco se elimino correctamente")
        return True