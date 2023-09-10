from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando
import os

class Fdisk(Comando):

    def __init__(self, parametros: dict) -> None:
        self.parametros = parametros

    def ejecutar(self):
        path_particion = self.parametros.get("path")
        size_particion = self.parametros.get("size")
        name = self.parametros.get("name")
        if path_particion == None or size_particion == None or name == None:
            print("Faltan parametros")
            return False
        if not os.path.isfile(path_particion):
            print("El disco no existe")
            return False
        if size_particion <= 0:
            print("El size_particion debe ser mayor a cero")
            return False  
        match self.parametros.get("unit", "K").upper():
            case "B":
                size_particion = size_particion
            case "K":
                size_particion *= 1024
            case "M":
                size_particion *= 1024 * 1024
            case _:
                print("Valor del parametro unit no valido")
                return False
        tipo_particion = self.parametros.get("type", "P").upper()
        if tipo_particion != "P" and tipo_particion != "E" and tipo_particion != "L":
            print("Valor del parametro type no es valido")
            return False
        fit_particion = self.parametros.get("fit", "WF").upper()
        if fit_particion != "BF" and fit_particion != "FF" and fit_particion != "WF":
            print("Valor del parametro fit_particion no es valido")
            return False
        fit_particion = fit_particion[0:1] #asi porque es un byte
        with open(path_particion, "rb+") as archivo_binario: #Recupero los valores de mbr
            estruct_mbr = Mbr(0, 0, 0, 0)
            estruct_mbr.set_bytes(archivo_binario) # valores del mbr recuperados
            if estruct_mbr.buscar_particion(name):
                print("El nombre ya existe para crear particion")
                return False
            # Creamos la particion
            if estruct_mbr.crear_particion(size_particion, name, tipo_particion, fit_particion, archivo_binario): #modifico el mbr y lo escribo de nuevo
                archivo_binario.seek(0)
                archivo_binario.write(estruct_mbr.get_bytes())
                print("---Particion creada")
                return True
        return False
        
        