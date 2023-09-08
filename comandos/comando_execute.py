from .comando_base import Comando

class Execute(Comando):

    def __init__(self, parametros: list, lexer, parser) -> None:
        self.parametros = parametros
        self.lexer = lexer
        self.parser = parser

    def ejecutar(self):
        self.lexer.lineno = 1
        if len(self.parametros) == 0:
            print('Faltan parametros')
            return False
        with open(self.parametros['path'], "r") as comandos:
            for linea in comandos.readlines():
                resultado = self.parser.parse(linea)
                if resultado != None:
                    print('--->Comando a punto ejecutar: ', linea)
                    resultado.ejecutar()
            #return comandos.readlines()