from .estructura_base import EstructuraBase

class ContenidoCarpeta(EstructuraBase):

    def __init__(self, name: str, inodo: int) -> None:
        self.name = name # 12 bytes str
        self.inodo = inodo # 4 bytes int apuntador a un inodo asociado al archivo o carpeta
    
    def set_bytes(self, archivo_binario=None):
        return super().set_bytes(archivo_binario)

class BloqueCarpetas(EstructuraBase):

    def __init__(self) -> None:
        self.contenido = [ContenidoCarpeta("", -1), ContenidoCarpeta("", -1),
                          ContenidoCarpeta("", -1), ContenidoCarpeta("", -1)]
    
    def set_bytes(self, archivo_binario=None):
        return super().set_bytes(archivo_binario)

class BloqueArchivos(EstructuraBase):

    def __init__(self, contenido: str) -> None:
        tamano = len(contenido)
        if tamano < 64:
            contenido += "\0"*(64-tamano)
        self.contenido = contenido # 64 bytes string
    
    def set_bytes(self, archivo_binario=None):
        return super().set_bytes(archivo_binario)

class BloqueApuntador(EstructuraBase):

    def __init__(self) -> None:
        self.punteros = [-1,-1,-1,-1,
                         -1,-1,-1,-1,
                         -1,-1,-1,-1,
                         -1,-1,-1,-1,
                         ] # 4 bytes int * 16 = 64 bytes
        
    def set_bytes(self, archivo_binario=None):
        return super().set_bytes(archivo_binario)