from abc import ABC, abstractmethod

class EstructuraBase(ABC):

    def get_bytes(self) -> bytearray:
        bytes = bytearray()
        for atributo, valor in vars(self).items():
            tipo = type(valor).__name__
            if tipo == 'int':
                bytes += valor.to_bytes(4, byteorder = 'big')
            elif tipo == 'str':
                bytes += valor.encode('utf-8')
            elif tipo == 'bool':
                bytes += valor.to_bytes(1, byteorder = 'big')
            elif tipo == 'list':
                for item in valor:
                    bytes += item.get_bytes()
            else:
                bytes += valor.get_bytes()
        return bytes
    
    @abstractmethod
    def set_bytes(self, bytes: bytes):
        pass