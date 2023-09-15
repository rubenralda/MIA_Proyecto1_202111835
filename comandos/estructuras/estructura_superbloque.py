from .estructura_base import EstructuraBase
from .estructura_bloques import *
from .estructura_tabla_inodos import *
from math import floor, ceil
import time

tamano_journaling = 33

class SuperBloque(EstructuraBase):

    def __init__(self, filesystem: int, start: int, size: int) -> None:
        self.filesystem_type = filesystem # 4 bytes int, 0 = ext2 y  1 = ext3
        n = (size - 68) / (tamano_journaling*filesystem + 4 + 92 + 3*64) # si es ext3 se suma el size del journaling
        numero_structuras = floor(n)

        self.inodos_count = numero_structuras # 4 bytes int
        self.bloque_count = numero_structuras * 3  # 4 bytes int
        self.inodos_libres_count = numero_structuras # 4 bytes int
        self.bloque_libres_count = numero_structuras * 3  # 4 bytes int

        self.tiempo_montado = 0 # 4 bytes int
        self.tiempo_desmontado = 0 # 4 bytes int
        self.conteo_montadas = 0 # 4 bytes int
        
        self.magic = 61299 # 4 bytes int 0xEF53
        self.tamano_inodo = 92 # 4 bytes int
        self.tamano_bloque = 64 # 4 bytes int

        self.primer_inodo_libre = 2 # 4 bytes int
        self.primer_bloque_libre = 2 # 4 bytes int
        self.bitmap_inodo_start = start + 68 + tamano_journaling*self.filesystem_type # 4 bytes int
        self.bitmap_bloque_start = self.bitmap_inodo_start + numero_structuras # 4 bytes int
        self.inodo_start = self.bitmap_bloque_start + 3*numero_structuras# 4 bytes int
        self.bloque_start = self.inodo_start + numero_structuras*self.tamano_inodo # 4 bytes int

    def set_bytes(self, archivo_binario=None):
        bytes = archivo_binario.read(68)
        self.filesystem_type = int.from_bytes(bytes[0:4], byteorder = 'big')
        self.inodos_count = int.from_bytes(bytes[4:8], byteorder = 'big')
        self.bloque_count = int.from_bytes(bytes[8:12], byteorder = 'big')
        self.inodos_libres_count = int.from_bytes(bytes[12:16], byteorder = 'big')
        self.bloque_libres_count = int.from_bytes(bytes[16:20], byteorder = 'big')
        self.tiempo_montado = int.from_bytes(bytes[20:24], byteorder = 'big')
        self.tiempo_desmontado = int.from_bytes(bytes[24:28], byteorder = 'big')
        self.conteo_montadas = int.from_bytes(bytes[28:32], byteorder = 'big')
        self.magic = int.from_bytes(bytes[32:36], byteorder = 'big')
        self.tamano_inodo = int.from_bytes(bytes[36:40], byteorder = 'big')
        self.tamano_bloque = int.from_bytes(bytes[40:44], byteorder = 'big')
        self.primer_inodo_libre = int.from_bytes(bytes[44:48], byteorder = 'big')
        self.primer_bloque_libre = int.from_bytes(bytes[48:52], byteorder = 'big')
        self.bitmap_inodo_start = int.from_bytes(bytes[52:56], byteorder = 'big')
        self.bitmap_bloque_start = int.from_bytes(bytes[56:60], byteorder = 'big')
        self.inodo_start = int.from_bytes(bytes[60:64], byteorder = 'big')
        self.bloque_start = int.from_bytes(bytes[64:68], byteorder = 'big')

    def crear_archivo(self, archivo_binario, size: int, path: str, r:bool):
        # seek en posicion despues del superbloque
        # bitmap inician desde 0
        bloques_archivo = ceil(size / self.tamano_bloque) #numero de bloques
        if bloques_archivo >= self.bloque_libres_count:
            print("--Error: La particion esta llena--")
        inodo_raiz = Inodos()
        inodo_raiz.uid = 1
        inodo_raiz.gid = 1
        inodo_raiz.size = 0
        inodo_raiz.atime = int(time.time())
        inodo_raiz.ctime = int(time.time())
        inodo_raiz.mtime= int(time.time())
        inodo_raiz.tipo = 0
        inodo_raiz.permiso = 600
        inodo_raiz.bloque[0] = 0
    
    def utilizar_un_bloque(self, archivo_binario): 
        # actualizar el bitmap de bloques
        archivo_binario.seek(self.bitmap_bloque_start + self.primer_bloque_libre) # estoy en el byte libre
        archivo_binario.write(bytes([1])) # indico que esta ocupado
        for i in range(self.bitmap_bloque_start + self.primer_bloque_libre + 1, self.inodo_start): # busco el siguiente libre
            es_vacio = not bool(int.from_bytes(archivo_binario.read(1)[0:1], byteorder= 'big'))
            if es_vacio:
                archivo_binario.seek(-1, 1) # regreso al que lei
                archivo_binario.write(bytes([1]))
                self.primer_bloque_libre = i  - self.bitmap_bloque_start # obtengro el valor del bloque
                self.bloque_libres_count -= 1 # resto el nuevo bloque
                break

    def utilizar_un_inodo(self, archivo_binario):
        # actualizar el bitmap de inodos
        archivo_binario.seek(self.bitmap_inodo_start + self.primer_inodo_libre) # estoy en el byte libre
        archivo_binario.write(bytes([1])) # indico que esta ocupado
        for i in range(self.bitmap_inodo_start + self.primer_inodo_libre + 1, self.bitmap_bloque_start): # busco el siguiente libre
            es_vacio = not bool(int.from_bytes(archivo_binario.read(1)[0:1], byteorder= 'big'))
            if es_vacio:
                archivo_binario.seek(-1, 1) # regreso al que lei
                archivo_binario.write(bytes([1]))
                self.primer_inodo_libre = i  - self.bitmap_inodo_start # obtengro el nuevo inodo libre
                self.inodos_libres_count -= 1 # resto el nuevo inodo
                break

    def reporte_sb(self):
        fileSystem = "EXT2"
        if self.filesystem_type == 1:
            fileSystem = "EXT3"
        reporte = '''digraph reporte_del_mbr_ff {{
    node [shape=plaintext]
    mbr [
        label=<
            <table border="0" cellborder="1" cellspacing="0">
                <tr>
                    <td bgcolor="/rdylgn6/5:/rdylgn6/5" COLSPAN="2"><b>REPORTE DE SUPERBLOQUE</b></td>
                </tr>
                <tr>
                    <td>File System type</td><td>{}</td>
                </tr>
                <tr>
                    <td>Cantidad i-nodos</td><td>{}</td>
                </tr>
                <tr>
                    <td>Cantidad bloques</td><td>{}</td>
                </tr>
                <tr>
                    <td>Cantidad i-nodos libres</td><td>{}</td>
                </tr>
                <tr>
                    <td>Cantidad bloques libres</td><td>{}</td>
                </tr>
                <tr>
                    <td>Ultimo montaje</td><td>{}</td>
                </tr>
                <tr>
                    <td>Ultimo desmontaje</td><td>{}</td>
                </tr>
                <tr>
                    <td>Conteo montajes</td><td>{}</td>
                </tr>
                <tr>
                    <td>Magic</td><td>{}</td>
                </tr>
                <tr>
                    <td>Tamano i-nodo</td><td>{}</td>
                </tr>
                <tr>
                    <td>Tamano bloque</td><td>{}</td>
                </tr>
                <tr>
                    <td>Primer i-nodo libre</td><td>{}</td>
                </tr>
                <tr>
                    <td>Primer bloque libre</td><td>{}</td>
                </tr>
                <tr>
                    <td>Inicio Bitmap de i-nodos</td><td>{}</td>
                </tr>
                <tr>
                    <td>Inicio Bitmap de bloques</td><td>{}</td>
                </tr>
                <tr>
                    <td>Inicio de i-nodos</td><td>{}</td>
                </tr>
                <tr>
                    <td>Inicio de bloques</td><td>{}</td>
                </tr>'''.format(fileSystem, str(self.inodos_count), str(self.bloque_count), str(self.inodos_libres_count),
                                str(self.bloque_libres_count), time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(self.tiempo_montado)),
                                time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(self.tiempo_desmontado)), str(self.conteo_montadas),
                                str(self.magic), str(self.tamano_inodo), str(self.tamano_bloque), str(self.primer_inodo_libre),
                                str(self.primer_bloque_libre), str(self.bitmap_inodo_start), str(self.bitmap_bloque_start),
                                str(self.inodo_start), str(self.bloque_start))
        reporte += '''</table>
            >];
        }'''
        return reporte
    
    def reporte_bm_inodo(self, archivo_binario):
        reporte = ""
        archivo_binario.seek(self.bitmap_inodo_start)
        for i in range(self.bitmap_inodo_start, self.bitmap_bloque_start):
            valor = str(int.from_bytes(archivo_binario.read(1)[0:1], byteorder= 'big'))
            reporte += valor
            if i % 20 == 0:
                reporte += "\n"
        return reporte
    
    def reporte_bm_bloc(self, archivo_binario):
        reporte = ""
        archivo_binario.seek(self.bitmap_bloque_start)
        for i in range(self.bitmap_bloque_start, self.inodo_start):
            valor = str(int.from_bytes(archivo_binario.read(1)[0:1], byteorder= 'big'))
            reporte += valor
            if i % 20 == 0:
                reporte += "\n"
        return reporte
