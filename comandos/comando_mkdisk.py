from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando
import time
import random
import os

class Mkdisk(Comando):
    def __init__(self, parametros: dict):
        self.parametros = parametros

    def ejecutar(self):
        size = self.parametros.get("size")
        direccion = self.parametros.get("path")
        if size == None or direccion == None:
            print("--Error: Faltan parametros--")
            return False
        # Obtenemos el directorio de la ruta (sin el nombre del archivo)
        carpetas = os.path.dirname(direccion)
        # Verificar si el directorio no existe y crearlo si es necesario
        if not os.path.exists(carpetas):
            os.makedirs(carpetas)
        if size <= 0:
            print("--Error: El size debe ser mayor a cero--")
            return False
        match self.parametros.get("unit", "M").upper():
            case "K":
                size *= 1024
            case "M":
                size *= 1024 * 1024
            case _:
                print("--Error: Valor del parametro unit no valido--")
                return False
        
        fecha = int(time.time())
        signature = random.randint(1, 1000000)
        fit = self.parametros.get("fit", "FF").upper()
        if fit != "BF" and fit != "FF" and fit != "WF":
            print("--Error: Valor del parametro fit no es valido--")
            return False
        fit = fit[0:1] #asi porque es un byte
        estruct_mbr = Mbr(size, fecha, signature, fit)
       
        with open(direccion, "wb") as archivo_binario:
            archivo_binario.write(b'\x00'* size)

        with open(direccion, 'rb+') as archivo_binario:
            archivo_binario.write(estruct_mbr.get_bytes())

        print("\n--Archivo creado con éxito--\n")
        return True
       