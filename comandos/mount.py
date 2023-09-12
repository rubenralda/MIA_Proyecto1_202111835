particion_montadas = []
# direccion del disco de la particion
# objeto de la particion
# id de la particion


def obtener_particiones():
    return particion_montadas

def agregar_particion(particion):
    global particion_montadas
    particion_montadas.append(particion)
    return True