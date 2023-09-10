from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando
import time


class Rep(Comando):

    def ejecutar(self):
        with open("/home/rubenralda/escritorio/Disco1.dsk", "rb") as archivo_binario:
            estruct_mbr = Mbr(0, 0, 0, 0)
            estruct_mbr.set_bytes(archivo_binario)
        print("----Fecha y hora:", time.strftime("%Y-%m-%d %H:%M:%S",
              time.localtime(estruct_mbr.fecha)))
        print("----Tamaño total:", estruct_mbr.tamano, "bytes")
        print("----Fit:", estruct_mbr.fit)
        print("----Número de disco:", estruct_mbr.signature)
        i = 1
        for particion in estruct_mbr.particiones:
            if particion.status == "V":
                print(f"*-*Particion {i}*-*")
                print("--Name:", particion.name)
                print("--Tipo", particion.tipo)
                print("--Fit", particion.fit)
                print("--Inicio", particion.start)
                print("--Tamaño", particion.s)
            i += 1
        return True
