from .estructura_base import EstructuraBase

class Particion(EstructuraBase):

    def __init__(self, status: str, tipo: str, fit: str, start: int, s: int, name: str):
        self.status = status # 1 byte; V si esta activo, F contrario
        self.tipo = tipo # 1 byte
        self.fit = fit # 1 byte
        self.start = start # 4 bytes
        self.s = s # 4 bytes
        largo_nombre = len(name)
        while(largo_nombre < 16):
            name += "\0"
            largo_nombre += 1
        self.name = name # 16 bytes
    
    def set_bytes(self, bytes: bytes):
        self.status = bytes[0:1].decode('utf-8')
        self.tipo = bytes[1:2].decode('utf-8')
        self.fit = bytes[2:3].decode('utf-8')
        self.start = int.from_bytes(bytes[3:7], byteorder = 'big')
        self.s = int.from_bytes(bytes[7:11], byteorder = 'big')
        self.name = bytes[11:27].decode('utf-8')