from .comando_base import Comando

class Mount(Comando):

    def __init__(self, parametros: dict) -> None:
        self.parametros = parametros