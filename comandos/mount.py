import os

class Particiones_montadas:

    def __init__(self, id: str, particion, path_disco: str, tipo_particion: str, nombre: str) -> None:
        self.particion = particion
        self.path_disco = path_disco
        self.tipo_particion = tipo_particion
        self.id = id
        self.nombre= nombre

particion_montadas = []

def obtener_particiones():
    return particion_montadas

def agregar_particion(particion, path_disco:str, tipo: str, nombre: str):
    global particion_montadas
    numero_particion = 1
    for particion in particion_montadas:
        if particion.path_disco == path_disco:
            numero_particion += 1
    id = "35" + str(numero_particion) + os.path.splitext(os.path.basename(path_disco))[0]
    print(id)
    nueva_particion = Particiones_montadas(id, particion, path_disco, tipo, nombre)
    particion_montadas.append(nueva_particion)
    return True

def eliminar_montada(id: str):
    global particion_montadas
    for i, particion in enumerate(particion_montadas):
        if particion.id == id:
            particion_montadas.pop(i)
            return True
    return False