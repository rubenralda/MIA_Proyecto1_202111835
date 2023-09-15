from .estructura_base import EstructuraBase

class Journaling(EstructuraBase):

    def __init__(self) -> None:
        self.tipo_operacion = "" # 14 bytes string
        self.tipo = "" # 1 char
        self.nombre = "" # 14 bytes string
        self.contenido = ""
        self.fecha = 0 # 4 bytes int

    def set_bytes(self, archivo_binario=None):
        bytes = archivo_binario.read(34)
