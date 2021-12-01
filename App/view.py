"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf




servicefile_vertex = 'airports_full.csv'
servicefile_edges = 'routes_full.csv'
servicesfile_city = "worldcities.csv"
initialStation = None
sys.setrecursionlimit(2 ** 20)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def optionTwo():
    cont = controller.init()
    print("\nCargando información de transporte de singapur ....")
    analyzer,firstservice,lastcity=controller.loadServices(cont, servicefile_vertex, servicefile_edges,servicesfile_city)
    numedges = controller.totalConnectionsdi(analyzer)
    numvertex = controller.totalStopsdi(analyzer)
    print('Numero de vertices digrafo: ' + str(numvertex))
    print('Numero de arcos digrafo: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    numedges = controller.totalConnectionsno(analyzer)
    numvertex = controller.totalStopsno(analyzer)
    print('Numero de vertices grafo: ' + str(numvertex))
    print('Numero de arcos grafo: ' + str(numedges))
    numciu=controller.totalciu(analyzer)
    print('Numero de ciudades mapa: ' + str(numciu))
    print('Primer Aeropuerto: ' + str(firstservice))
    print('Última ciudad: ' + str(lastcity))



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexion aera")
    print("3- Encontrar Clusteres aereos")
    print("4- Encontrar la ruta mas corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aereopuerto cerrado")
    print("7- Comparar con servicio WEB externo")
    print("8- Visualizar graficamente los requerimientos")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        optionTwo()
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 3:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 4:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 5:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 6:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 7:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 8:
        print("Funcion en desarrollo...\n")

    else:
        sys.exit(0)
sys.exit(0)
