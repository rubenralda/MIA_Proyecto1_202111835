from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando

class Fdisk(Comando):

    def __init__(self, parametros: dict) -> None:
        self.parametros = parametros

    def ejecutar(self):
        direccion = self.parametros.get("path")
        size = self.parametros.get("size")
        name = self.parametros.get("name")
        if direccion == None or size == None or name == None:
            print("Faltan parametros")
            return False
        if size <= 0:
            print("El size debe ser mayor a cero")
            return False  
        match self.parametros.get("unit", "K").upper():
            case "B":
                size = size
            case "K":
                size *= 1024
            case "M":
                size *= 1024 * 1024
            case _:
                print("Valor del parametro unit no valido")
                return False
        tipo_particion = self.parametros.get("type", "P").upper()
        if tipo_particion != "P" and tipo_particion != "E" and tipo_particion != "L":
            print("Valor del parametro type no es valido")
            return False
        estruct_mbr = Mbr(0, 0, 0, 0)
        with open(direccion, "rb") as archivo_binario:
            bytes = archivo_binario.read(121)
            estruct_mbr.set_bytes(bytes) # valores del mbr recuperados
        # crear particion
        if estruct_mbr.buscar_particion(name):
            print("El nombre ya exite para crear particion")
            return False
        if estruct_mbr.crear_particion_bf(size, name, tipo_particion):
            with open(direccion, 'rb+') as archivo_binario:
                archivo_binario.write(estruct_mbr.get_bytes())
            print("---Particion creada")
            return True
        return False
        
        