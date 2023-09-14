from .estructura_base import EstructuraBase
from math import floor

tamano_journaling = 33

class SuperBloque(EstructuraBase):

    def __init__(self, filesystem: int, start: int, size: int) -> None:
        self.filesystem_type = filesystem # 4 bytes int, 0 = ext2 y  1 = ext3
        n = (size - 68) / (tamano_journaling*filesystem + 4 + 92 + 3*64) # si es ext3 se suma el size del journaling
        numero_structuras = floor(n)

        self.inodos_count = numero_structuras # 4 bytes int
        self.bloque_count = numero_structuras * 3  # 4 bytes int
        self.inodos_libres_count = numero_structuras # 4 bytes int
        self.bloque_libres_count = numero_structuras * 3  # 4 bytes int
        self.tiempo_montado = 0 # 4 bytes int
        self.tiempo_desmontado = 0 # 4 bytes int
        self.conteo_montadas = 0 # 4 bytes int
        
        self.magic = 61299 # 4 bytes int 0xEF53
        self.tamano_inodo = 92 # 4 bytes int
        self.tamano_bloque = 64 # 4 bytes int

        self.primer_inodo_libre = 2 # 4 bytes int
        self.primer_bloque_libre = 2 # 4 bytes int
        self.bitmap_inodo_start = start + 68 + tamano_journaling*self.filesystem_type # 4 bytes int
        self.bitmap_bloque_start = self.bitmap_inodo_start + numero_structuras # 4 bytes int
        self.inodo_start = self.bitmap_bloque_start + 3*numero_structuras# 4 bytes int
        self.bloque_start = self.inodo_start + numero_structuras*self.tamano_inodo # 4 bytes int

    def set_bytes(self, archivo_binario=None):
        bytes = archivo_binario.read(68)
        self.filesystem_type = int.from_bytes(bytes[0:4], byteorder = 'big')
        self.inodos_count = int.from_bytes(bytes[4:8], byteorder = 'big')
        self.bloque_count = int.from_bytes(bytes[8:12], byteorder = 'big')
        self.inodos_libres_count = int.from_bytes(bytes[12:16], byteorder = 'big')
        self.bloque_libres_count = int.from_bytes(bytes[16:20], byteorder = 'big')
        self.tiempo_montado = int.from_bytes(bytes[20:24], byteorder = 'big')
        self.tiempo_desmontado = int.from_bytes(bytes[24:28], byteorder = 'big')
        self.conteo_montadas = int.from_bytes(bytes[28:32], byteorder = 'big')
        self.magic = int.from_bytes(bytes[32:36], byteorder = 'big')
        self.tamano_inodo = int.from_bytes(bytes[36:40], byteorder = 'big')
        self.tamano_bloque = int.from_bytes(bytes[40:44], byteorder = 'big')
        self.primer_inodo_libre = int.from_bytes(bytes[44:48], byteorder = 'big')
        self.primer_bloque_libre = int.from_bytes(bytes[48:52], byteorder = 'big')
        self.bitmap_inodo_start = int.from_bytes(bytes[52:56], byteorder = 'big')
        self.bitmap_bloque_start = int.from_bytes(bytes[56:60], byteorder = 'big')
        self.inodo_start = int.from_bytes(bytes[60:64], byteorder = 'big')
        self.bloque_start = int.from_bytes(bytes[64:68], byteorder = 'big')