import csv
import time
import os
from random import*
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
with open("sueldos.csv","w",newline='') as sueldos_csv: 
    registro_csv = csv.writer(sueldos_csv)
    
    
def menu():
    
    while True:
         try:
            print(("-----Bienvenido al menu de sueldos----- \n\n Por favor ingrese una de las siguientes opciones: \n\n 1|Asignar Sueldos Aleatorio. \n 2|Clasificar Sueldos. \n 3|Ver estadisticas. \n 4|Reporte de Sueldos. \n 5|Salir del Programa. "))
            opc=int(input("Ingrese su Opción"))
            if opc=1 
            