import codecs #importamos codecs

class MiArchivo: #clase  para leer el archivo con los datos
    """
    """
    
    def __init__(self): #innit donde inicializamos el archivo con el archivo informacion
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self): #metodo obtener informacion
        return self.archivo.readlines() # nos retorna toda la informacion del archivo 

    def cerrar_archivo(self): #metodo para cerrar el archivo
        self.archivo.close()


class MiArchivoEscribir: #clase donde agregamos valores a un nuevo archivo
    """
    """
    
    def __init__(self): #init donde inicializamos  el archivo vacio y  el  atributo a para agregar
        """
        """
        self.archivo = codecs.open("data/info.csv", "a")

    def agregar_informacion(self, p): #metodo agregar informacion donde  escribimos  el nombre y el promedio
        self.archivo.write("%s|%s|%s|%s\n" % (p.obtener_nombre(), p.obtener_ciudad(),p.obtener_campeonatos(),p.obtener_njugadores()))

    def cerrar_archivo(self): #metodo para cerrar el archivo
        self.archivo.close()
