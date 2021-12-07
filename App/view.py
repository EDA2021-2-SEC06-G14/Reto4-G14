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
from prettytable import PrettyTable, ALL
from time import process_time
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(2 ** 20)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def Carga(catalog):
    
    firstservice1, lastservice1, firstcity, lastcity = controller.loadServices(catalog)
    veritces1 = controller.getNumVertices(catalog["conect_digraph"])
    veritces2 = controller.getNumVertices(catalog["conect_normgraph"])
    arcos1 = controller.getNumArcos(catalog["conect_digraph"])
    arcos2 = controller.getNumArcos(catalog["conect_normgraph"])
    sizemap = controller.getMapSize(catalog["cities"])
    

    x = PrettyTable()
    x.field_names = (["IATA", "Name", "City", "Country", "Latitude", "Longitude"])
    x.max_width = 25
    x.hrules = ALL
    x.add_row([firstservice1["IATA"], firstservice1["Name"], firstservice1["City"], firstservice1["Country"], firstservice1["Latitude"], firstservice1["Longitude"]])
    x.add_row([lastservice1["IATA"], lastservice1["Name"], lastservice1["City"], lastservice1["Country"], lastservice1["Latitude"], lastservice1["Longitude"]])

    y = PrettyTable()
    y.field_names = (["IATA", "Name", "City", "Country", "Latitude", "Longitude"])
    y.max_width = 25
    y.hrules = ALL
    y.add_row([firstservice1["IATA"], firstservice1["Name"], firstservice1["City"], firstservice1["Country"], firstservice1["Latitude"], firstservice1["Longitude"]])
    y.add_row([lastservice1["IATA"], lastservice1["Name"], lastservice1["City"], lastservice1["Country"], lastservice1["Latitude"], lastservice1["Longitude"]])


    z = PrettyTable()
    z.field_names = (["City", "Country", "Latitude", "Longitude", "Population"])
    z.max_width = 25
    z.hrules = ALL
    z.add_row([firstcity["city_ascii"], firstcity["country"], firstcity["lat"], firstcity["lng"], firstcity["population"]])
    z.add_row([lastcity["city_ascii"], lastcity["country"], lastcity["lat"], lastcity["lng"], lastcity["population"]])

    print("=== Airports-Routes DiGraph ===")
    print("Nodes: " + str(veritces1))
    print("Edges: " + str(arcos1))
    print("First and Last Airport loaded in the Graph: ")
    print(x)
    print("=== Airports-Routes Graph ===")
    print("Nodes: " + str(veritces2))
    print("Edges: " + str(arcos2))
    print("First and Last Airport loaded in the Graph: ")
    print(y)
    print("=== City Network ===")
    print("The number of cities are: " + str(sizemap))
    print("First and Last Cities loaded in the data structure: ")
    print(z)

def reqUno(catalog):
    data = controller.reqUno(catalog)
    data = lt.subList(data,1,5)
    data = lt.iterator(data)
    conectados = controller.numConecados(catalog)
    veritces = controller.getNumVertices(catalog["conect_digraph"])
    x = PrettyTable()
    x.field_names = (["Name", "City", "Country", "IATA", "Conections", "Inbound", "Outbound"])
    x.max_width = 25
    x.hrules = ALL
    
    for i in data:
        x.add_row([i["airport"]["Name"], i["airport"]["City"], i["airport"]["Country"], i["airport"]["IATA"], i["edges"], i["IN"], i["OUT"]])


    print("========== Req No. 1 Inputs ==========")
    print("Most connected airports in network (TOP 5)")
    print("Number of airports in network: " + str(veritces) + "\n")
    print("========== Req No. 1 Answer ==========")
    print("Connected airports inside network: " + str(conectados))
    print("TOP 5 most connected airports... \n")
    print(x)



def reqDos(catalog, aereo1, aereo2):
    data = controller.reqDos(catalog, aereo1, aereo2)
    a1 = controller.GetAirport(catalog, aereo1)
    a2 = controller.GetAirport(catalog, aereo2)

    x = PrettyTable()
    x.field_names = (["IATA", "Name", "City", "Country"])
    x.max_width = 25
    x.hrules = ALL
    x.add_row([aereo1, a1["Name"], a1["City"], a1["Country"]])

    y = PrettyTable()
    y.field_names = (["IATA", "Name", "City", "Country"])
    y.max_width = 25
    y.hrules = ALL
    y.add_row([aereo2, a2["Name"], a2["City"], a2["Country"]])

    print("==========Req No.2 Inputs==========")
    print("Airport-1 IATA code: " + aereo1)
    print("Airport-2 IATA code: " + aereo2)
    print("==========Req No.2 Answer==========")
    print("+++ Airport IATA code: " + aereo1 + " +++")
    print(x)
    print("+++ Airport IATA code: " + aereo2 + " +++")
    print(y)
    print("- Number of SCC in Airport-Route network: " + str(data[0]))
    print("- Does the \'" + a1["Name"] + "\' and the \'" + a2["Name"] + "\' belong together?")
    print("- ANS: " + str(data[1]))


def reqCuatro(catalog, origen, millas):
    data = controller.reqCuatro(catalog, origen, millas)




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
    inputs = input('Seleccione una opción para continuar\n >')
    if int(inputs[0]) == 1:
        t1 = process_time()
        catalog = controller.init()
        print("Cargando información de los archivos ....")
        Carga(catalog)
        t2 = process_time()
        print("Time = " + str(t2-t1)+"seg\n")

    elif int(inputs[0]) == 2:
        t1 = process_time()
        reqUno(catalog)
        t2 = process_time()
        print("Time = " + str(t2-t1)+"seg\n")

    elif int(inputs[0]) == 3:
        aereo1 = input("Codigo IATA del aereopuerto 1: \n >")
        aereo2 = input("Codigo IATA del aereopuerto 2: \n >")
        t1 = process_time()
        reqDos(catalog, aereo1, aereo2)
        t2 = process_time()
        print("Time = " + str(t2-t1)+"seg\n")

    elif int(inputs[0]) == 4:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 5:
        origen = input("Aereopuerto de origen: \n >")
        millas = input("Millas disponibles para el viaje: \n >")
        reqCuatro(catalog, origen, millas)
    elif int(inputs[0]) == 6:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 7:
        print("Funcion en desarrollo...\n")

    elif int(inputs[0]) == 8:
        print("Funcion en desarrollo...\n")

    else:
        sys.exit(0)
sys.exit(0)
