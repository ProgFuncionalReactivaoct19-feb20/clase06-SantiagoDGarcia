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
	datos = list(lineasDiccionario(midata))
	fun1 = lambda x: list(x.items())[0][1]
	print(list(map(fun1, datos)))
