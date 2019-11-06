"""
    @SantiagoDGarcia
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv


def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")
# Extrae os datos en diccionarios...

with open("data/data-estudiantes.csv") as midata:
	# Se separan los datos en diccionarios
	datos = list(lineasDiccionario(midata))
	"""

	VERSION1
	# Se determina la funcion para sacar los nombres
	fun1 = lambda x: list(x.items())[0][1]
	cadena1 = (list(map(fun1, datos)))
	# Se separan los nombres de la cadena por espacios
	nomb1 = map(lambda x: x.split(" "), cadena1)
	#
	# Se escogen los correos 
	fun2 = lambda x: list(x.items())[1][1]
	# Se separan los datos en una variable para ser usados
	cadena2 = (list(map(fun2, datos)))
	# Se escogen los datos del correo separando las variables por medio del punto
	correo = map(lambda x: x.split("."), cadena2)
	correo1 = map(lambda x: x[0], correo)
	correoF = (list(correo1))

	print(list(map(lambda x,y: x[0]+" - "+ y, nomb1, correoF)))
	"""

	print(list(map(lambda x: "%s -  %s" % (list(x.items())[0][1].split(" ")[1],list(x.items())[1][1].split(".")[0]), datos))) 

	
