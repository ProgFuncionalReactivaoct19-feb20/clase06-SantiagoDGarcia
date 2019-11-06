"""
    @SantiagoDGarcia
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv


def lineas(archivo):
	return csv.DictReader(archivo, delimiter="\t")
# Extrae los datos en diccionarios...

with open("data/trabajadores.csv") as midata:
	# Se separan los datos en diccionarios
	datos = list(lineas(midata))
	# Se filtran los paises con mas de 10 palabras
	fun1 = filter(lambda x: len(list(x.items())[2][1])>= 10, datos)
	# Se guarda el progreso en una variable
	paises = (list(fun1)) 
	#Se separan las fechas mediante el guion y se ordenan
	orden = sorted( paises, key=lambda x: list(x.items())[1][1].split("-")[2])
	
	print(list(orden))

	

	
