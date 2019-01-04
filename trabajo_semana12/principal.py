from paqueteArchivo.miarchivo import MiArchivo, MiArchivoEscribir #importacion de los paquetec con sus respectivas clases
from paqueteModelo.mimodelo import Equipo,Operaciones

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion() #lista le mandamos  la informacion de el metodo obtener informacion
lista = [l.split("|") for l in lista] #manejo de split para cojer un elemento  donde termina en |
lista_equipos = []
for d in lista: #for para recorrer la lista
    
    e = Equipo(d[0], d[1],d[2],d[3]) #al objeto le mandamos los parametos de a lista  en tal posicion
    #print(e) #presenta el objeto p 
    lista_equipos.append(e)
    


opt = input("Desea ordenar por campeonatos (a)  o por numero de jugadores (b) ") #pregunta al usuario como debe ordenar(recibe una letra)
if opt == "a":
	operaciones = Operaciones(lista_equipos)
	print(operaciones.ordenar_campeonatos()) #presenta la lista ordenada
	m2.agregar_informacion(e) #agrega 
elif opt == "b":
	operaciones = Operaciones(lista_equipos)
	print(operaciones.ordenar_njugadores()) #presenta la lista rdenada
	m2.agregar_informacion(e) #agrega 
else:
	print("letra incorrecta")




m.cerrar_archivo() #metodo para cerrar el archivo  (close())
m2.cerrar_archivo() #cerrar el archivo que escribimos (close())
