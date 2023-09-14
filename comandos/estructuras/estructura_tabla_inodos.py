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
        self.bloque = [] # 4 * 15 registros int
        for _ in range(15):
            self.bloque.append(-1)
        self.tipo = 0 # 4 int 1 = archivo y 0 = carpeta
        self.permiso = 0 # 4 int