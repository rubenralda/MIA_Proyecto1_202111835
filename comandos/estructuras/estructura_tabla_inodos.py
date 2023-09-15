from .estructura_base import EstructuraBase
import time

class Inodos(EstructuraBase):

    def __init__(self) -> None:
        self.uid = 1 # 4 int usuario id
        self.gid = 1 # 4 int grupo id
        self.size = 0 # 4 int
        self.atime = int(time.time()) # 4 int
        self.ctime = int(time.time()) # 4 int
        self.mtime = int(time.time()) # 4 int
        self.tipo = 0 # 4 int 1 = archivo y 0 = carpeta
        self.permiso = 0 # 4 int
        self.bloque = [] # 4 * 15 registros int
        for _ in range(15):
            self.bloque.append(-1)
    
    def set_bytes(self, archivo_binario):
        bytes = archivo_binario.read(92)
        self.uid = int.from_bytes(bytes[0:4], byteorder = 'big')
        self.gid = int.from_bytes(bytes[4:8], byteorder = 'big')
        self.size = int.from_bytes(bytes[8:12], byteorder = 'big')
        self.atime = int.from_bytes(bytes[12:16], byteorder = 'big')
        self.ctime = int.from_bytes(bytes[16:20], byteorder = 'big')
        self.mtime = int.from_bytes(bytes[20:24], byteorder = 'big')
        self.tipo = int.from_bytes(bytes[24:28], byteorder = 'big')
        self.permiso = int.from_bytes(bytes[28:32], byteorder = 'big')
        for i in range(15):
            self.bloque[i] = int.from_bytes(bytes[32+4*i:36+4*i], byteorder = 'big', signed= True)