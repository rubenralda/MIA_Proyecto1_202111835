from .estructura_base import EstructuraBase

class ContenidoCarpeta(EstructuraBase):

    def __init__(self, name: str, inodo: int) -> None:
        self.name = name # 12 bytes str
        self.inodo = inodo # 4 bytes int apuntador a un inodo asociado al archivo o carpeta

class BloqueCarpetas(EstructuraBase):

    def __init__(self) -> None:
        self.contenido = [ContenidoCarpeta("", -1), ContenidoCarpeta("", -1),
                          ContenidoCarpeta("", -1), ContenidoCarpeta("", -1)]

class BloqueArchivos(EstructuraBase):

    def __init__(self) -> None:
        self.contenido = "" # 64 bytes string

class BloqueApuntador(EstructuraBase):

    def __init__(self) -> None:
        self.punteros = [-1,-1,-1,-1,
                         -1,-1,-1,-1,
                         -1,-1,-1,-1,
                         -1,-1,-1,-1,
                         ] # 4 bytes int * 16 = 64 bytes