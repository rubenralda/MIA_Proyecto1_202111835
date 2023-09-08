from .estructuras.estructura_mbr import Mbr
from .comando_base import Comando
import time


class Rep(Comando): 

    def ejecutar(self):
        with open("/home/rubenralda/Disco1.dsk", "rb") as archivo_binario:
            estruct_mbr = Mbr(0, 0, 0, 0)
            bytes = archivo_binario.read(121)
            estruct_mbr.set_bytes(bytes)
        print("----Fecha y hora:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(estruct_mbr.fecha)))
        print("----Tamaño total:", estruct_mbr.tamano, "bytes")
        print("----Fit:", estruct_mbr.fit)
        print("----Número de disco:", estruct_mbr.signature)
        if estruct_mbr.particion1.status == "V":
            print("*-*Particion 1*-*")
            print("--Name:", estruct_mbr.particion1.name)
            print("--Tipo", estruct_mbr.particion1.tipo)
            print("--Fit", estruct_mbr.particion1.fit)
            print("--Inicio", estruct_mbr.particion1.start)
            print("--Tamaño", estruct_mbr.particion1.s)
        if estruct_mbr.particion2.status == "V":
            print("*-*Particion 2*-*")
            print("--Name:", estruct_mbr.particion2.name)
            print("--Tipo", estruct_mbr.particion2.tipo)
            print("--Fit", estruct_mbr.particion2.fit)
            print("--Inicio", estruct_mbr.particion2.start)
            print("--Tamaño", estruct_mbr.particion2.s)
        if estruct_mbr.particion3.status == "V":
            print("*-*Particion 3*-*")
            print("--Name:", estruct_mbr.particion3.name)
            print("--Tipo", estruct_mbr.particion3.tipo)
            print("--Fit", estruct_mbr.particion3.fit)
            print("--Inicio", estruct_mbr.particion3.start)
            print("--Tamaño", estruct_mbr.particion3.s)
        if estruct_mbr.particion4.status == "V":
            print("*-*Particion 4*-*")
            print("--Name:", estruct_mbr.particion4.name)
            print("--Tipo", estruct_mbr.particion4.tipo)
            print("--Fit", estruct_mbr.particion4.fit)
            print("--Inicio", estruct_mbr.particion4.start)
            print("--Tamaño", estruct_mbr.particion4.s)
        return True
     