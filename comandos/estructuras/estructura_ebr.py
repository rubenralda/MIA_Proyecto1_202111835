from .estructura_base import EstructuraBase

class Ebr(EstructuraBase):

    def __init__(self, part_status: bool, part_fit: str, part_start: int, part_s: int, part_next:int, part_name:str) -> None:
        self.status = part_status # 1 byte True si esta activo
        self.fit = part_fit # 1 byte
        self.start = part_start # 4 byte empieza a contar desde el 0
        self.size = part_s # 4 byte
        self.siguiente = part_next # 4 byte
        largo_nombre = len(part_name)
        while(largo_nombre < 16):
            part_name += "\0"
            largo_nombre += 1
        self.name = part_name # 16 bytes

    def set_bytes(self, archivo_binario):
        bytes = archivo_binario.read(27)
        self.status = bytes[0:1].decode('utf-8')
        self.tipo = bytes[1:2].decode('utf-8')
        self.fit = bytes[2:3].decode('utf-8')
        self.start = int.from_bytes(bytes[3:7], byteorder = 'big')
        self.s = int.from_bytes(bytes[7:11], byteorder = 'big')
        self.name = bytes[11:27].decode('utf-8')