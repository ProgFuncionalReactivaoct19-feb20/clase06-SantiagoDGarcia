"""
    @SantiagoDGarcia
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter=";")
# Extrae los datos en una list
with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata)))

# midata = open("data/data-estudiantes.csv") # en usos de garndes volumenes de
	#datos es necesario cerrar el archivo"
#print(list(lineas(midata)))
#midata.close()