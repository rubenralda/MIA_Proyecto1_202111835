from .estructura_base import EstructuraBase
from .estructura_particion import Particion

class Mbr(EstructuraBase): 

    def __init__(self, tamano: int, fecha: int, signature: int, fit: str) -> None:
        self.tamano = tamano # 4 bytes 
        self.fecha = fecha # 4 bytes
        self.signature = signature # 4 bytes
        self.fit = fit # 1 byte
        self.particion1 = Particion("F", "P", "W", 0, 0, "")
        self.particion2 = Particion("F", "P", "W", 0, 0, "")
        self.particion3 = Particion("F", "P", "W", 0, 0, "")
        self.particion4 = Particion("F", "P", "W", 0, 0, "")

    def set_bytes(self, bytes: bytes):
        self.tamano = int.from_bytes(bytes[0:4], byteorder = 'big')
        self.fecha = int.from_bytes(bytes[4:8], byteorder = 'big')
        self.signature = int.from_bytes(bytes[8:12], byteorder = 'big')
        self.fit = bytes[12:13].decode("utf-8")
        self.particion1.set_bytes(bytes[13:40])
        self.particion2.set_bytes(bytes[40:67])
        self.particion3.set_bytes(bytes[67:94])
        self.particion4.set_bytes(bytes[94:121])

    # True si existe, False si no
    def buscar_particion(self, name: str):
        if self.particion1.name == name:
            return True
        if self.particion2.name == name:
            return True
        if self.particion3.name == name:
            return True
        if self.particion4.name == name:
            return True
        return False
    
    # Crea una particion con primer ajuste
    def crear_particion_bf(self, size: int, name: str, tipo_particion: str):
        start = 122 # tamaño del mbr bytes + 1
        if self.particion1.status == "F":
            if self.particion2.status == "V":
                if size + start >= self.particion2.start:
                    return False
            elif self.particion3.status == "V":
                if size + start >= self.particion3.start:
                    return False
            elif self.particion4.status == "V":
                if size + start >= self.particion4.start:
                    return False
            elif size + start > self.tamano:
                    return False
            particion = self.particion1
        elif self.particion2.status == "F":
            start = self.particion1.start + self.particion1.s
            if self.particion3.status == "V":
                if size + start >= self.particion3.start:
                    return False
            elif self.particion4.status == "V":
                if size + start >= self.particion4.start:
                    return False
            elif size + start > self.tamano:
                    return False
            particion = self.particion2
        elif self.particion3.status == "F":
            start = self.particion2.start + self.particion2.s
            if self.particion4.status == "V":
                if size + start >= self.particion4.start:
                    return False
            elif size + start > self.tamano:
                    return False
            particion = self.particion3
        elif self.particion4.status == "F":
            start = self.particion3.start + self.particion3.s
            if size + start > self.tamano:
                    return False
            particion = self.particion4
        else:
            return False
        particion.status = "V"
        particion.tipo = tipo_particion
        particion.start = start
        particion.s = size
        largo_nombre = len(name)
        while(largo_nombre < 16):
            name += "\0"
            largo_nombre += 1
        particion.name = name
        return True
            