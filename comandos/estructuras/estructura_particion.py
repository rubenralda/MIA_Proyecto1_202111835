from .estructura_base import EstructuraBase
from .estructura_ebr import Ebr

class Particion(EstructuraBase):

    def __init__(self, status: str, tipo: str, fit: str, start: int, s: int, name: str):
        self.status = status # 1 byte; V si esta activo, F contrario
        self.tipo = tipo # 1 byte
        self.fit = fit # 1 byte
        self.start = start # 4 bytes empieza a contar desde 0
        self.s = s # 4 bytes (size_particion) 
        largo_nombre = len(name)
        while(largo_nombre < 16):
            name += "\0"
            largo_nombre += 1
        self.name = name # 16 bytes
    
    def set_bytes(self, archivo_binario):
        bytes = archivo_binario.read(27)
        self.status = bytes[0:1].decode('utf-8')
        self.tipo = bytes[1:2].decode('utf-8')
        self.fit = bytes[2:3].decode('utf-8')
        self.start = int.from_bytes(bytes[3:7], byteorder = 'big')
        self.s = int.from_bytes(bytes[7:11], byteorder = 'big')
        self.name = bytes[11:27].decode('utf-8')

    def crear_extendida(self, archivo_binario):
        if self.tipo != "E":
            return
        estructura_ebr = Ebr(False, "W", self.start, 0, -1, "")
        archivo_binario.seek(self.start)
        archivo_binario.write(estructura_ebr.get_bytes())

    def crear_particion_logica(self, archivo_binario, particion:Ebr):
        if self.tipo != "E":
            print("--Error: No se puede crear la particion logica--")
            return False
        estructura_ebr = Ebr(False, "W", self.start, 0, -1, "")
        archivo_binario.seek(self.start)
        estructura_ebr.set_bytes(archivo_binario)
        if not estructura_ebr.status:
            # falta comprobar si despues de eliminar la primera particion que busque si cabe en este espacio
            # por el momento si esta vacia siempre va escribir aqui independiente del fit
            particion.start = self.start
            particion.siguiente = estructura_ebr.siguiente
            archivo_binario.seek(self.start)
            archivo_binario.write(particion.get_bytes())
            print("\n--Particion logica creada--\n")
            return True
        else:
            tamano_particion = self.start + self.s
            if self.fit == "F":
                estructura_ebr.crear_particion_siguiente_ff(archivo_binario, particion, tamano_particion)
            elif self.fit == "B":
                estructura_ebr.crear_particion_siguiente_bf(archivo_binario, particion, tamano_particion, tamano_particion, estructura_ebr)
            elif self.fit == "W":
                estructura_ebr.crear_particion_siguiente_wf(archivo_binario, particion, tamano_particion, 0, estructura_ebr)
            return True
    
    def buscar_particion_logica(self, name: str, archivo_binario):
        if self.tipo != "E":
            return False
        estructura_ebr = Ebr(False, "W", self.start, 0, -1, "")
        archivo_binario.seek(self.start)
        estructura_ebr.set_bytes(archivo_binario)
        return estructura_ebr.buscar_particion(name, archivo_binario)
    
    def eliminar_particion_logica(self, name:str, archivo_binario):
        if self.tipo != "E":
            return False
        estructura_ebr = Ebr(False, "W", self.start, 0, -1, "")
        archivo_binario.seek(self.start)
        estructura_ebr.set_bytes(archivo_binario)
        if estructura_ebr.status:
            if estructura_ebr.name == name:
                estructura_ebr.status = False
                # cambio el inicial
                archivo_binario.seek(self.start)
                archivo_binario.write(estructura_ebr.get_bytes())
                return True
        return estructura_ebr.eliminar_particion(name, archivo_binario)
    
    def add_particion_logica(self, name: str, archivo_binario, add: str):
        if self.tipo != "E":
            return False
        estructura_ebr = Ebr(False, "W", self.start, 0, -1, "")
        archivo_binario.seek(self.start)
        estructura_ebr.set_bytes(archivo_binario)
        return estructura_ebr.add_particion(name, archivo_binario, add, self.s)