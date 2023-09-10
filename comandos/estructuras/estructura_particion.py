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