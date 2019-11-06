"""
    @SantiagoDGarcia
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	datos = list(lineas(midata))

	#fun1 = filter(lambda x: x[1]!= "email", datos)
	# la funcion lamda es primero....
	print(list(map(lambda x: x[1], filter(lambda x: x[1]!= "email", datos))))



# midata = open("data/data-estudiantes.csv") # en usos de garndes volumenes de
	#datos es necesario cerrar el archivo"
#print(list(lineas(midata)))
#midata.close()