"""
    creación de clases
"""

class Equipo(object): #clase persona
    """
    """
    
    def __init__(self, n, c ,camp ,njug): #init con tods sus valores inicializados
        """
        """
        self.nombre = n
        self.ciudad = c
        self.campeonatos = int(camp)
        self.njugadores = int(njug)
    
    #METODOS AGREGAR Y OBTENER
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    
    def agregar_ciudad(self, c):
        """
        """
        self.ciudad = c

    def obtener_ciudad(self):
        """
        """
        return self.ciudad
    
    def agregar_campeonatos(self, camp):
        """
        """
        self.campeonatos = camp

    def obtener_campeonatos(self):
        """
        """
        return self.campeonatos

    def agregar_njugadores(self, njug):
        """
        """
        self.njugadores = njug

    def obtener_njugadores(self):
        """
        """
        return self.njugadores

    
    def __str__(self): #metodo to string
        """
        """
        return "Nombre:%s  Ciudad:%s  Campeonatos:%d Numero de jugadores:%d\n" % (self.obtener_nombre(), self.obtener_ciudad(),self.obtener_campeonatos(),self.obtener_njugadores()) #retorna una cadena (print)

    def __repr__(self): #metodo to string
        """
        """
        return "Nombre:%s  Ciudad:%s  Campeonatos:%d Numero de jugadores:%d\n" % (self.obtener_nombre(), self.obtener_ciudad(),self.obtener_campeonatos(),self.obtener_njugadores()) #retorna una cadena (print)


class Operaciones(object):
    """docstring for Operaciones"""
    def __init__(self, listado):

        self.listado_equipos = listado

    def ordenar_campeonatos(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_equipos, key=lambda equipo: equipo.campeonatos)

    def ordenar_njugadores(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_equipos, key=lambda equipo: equipo.njugadores)