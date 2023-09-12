from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando
from .mount import obtener_particiones
from graphviz import Source
import time
import os

class Rep(Comando):

    def __init__(self, parametros: dict) -> None:
        self.parametros = parametros

    def ejecutar(self):
        path_particion = self.parametros.get("path")
        id = self.parametros.get("id")
        name = self.parametros.get("name")
        if path_particion == None or name == None or id == None:
            print("--Error: Faltan parametros--")
            return False
        # Obtenemos el directorio de la ruta (sin el nombre del archivo)
        carpetas = os.path.dirname(path_particion)
        # Verificar si el directorio no existe y crearlo si es necesario
        if not os.path.exists(carpetas):
            os.makedirs(carpetas)
        match name.lower():
            case "mbr":
                particiones = obtener_particiones()
                direccion = ""
                for particion in particiones:
                    if particion.id == id:
                        direccion = particion.path_disco
                if direccion == "":
                    print("--Error: El ID no existe--") 
                with open(direccion, "rb") as archivo_binario:
                    estruct_mbr = Mbr(0, 0, 0, 0)
                    estruct_mbr.set_bytes(archivo_binario)
                    reporte_graphviz = estruct_mbr.reporte_mbr(archivo_binario)
                    grafo = Source(reporte_graphviz, format = 'png')
                    # print(reporte_graphviz)
                    grafo.render(path_particion, view= True)
                return True
            case "disk":
                pass
            case _:
                print("--Error: el valor del parametro name es incorrecto--")
                return False
