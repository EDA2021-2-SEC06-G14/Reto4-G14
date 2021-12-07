"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

from math import degrees, dist
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadServices(catalog):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.
    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile_ver = cf.data_dir + 'airports-utf8-small.csv'
    input_file_ver = csv.DictReader(open(servicesfile_ver, encoding="utf-8"),
                                delimiter=",")
    firstservice1= None
    for todo in input_file_ver:
        if firstservice1==None:
            firstservice1=todo
        iata= todo["IATA"]
        model.addAirport(catalog, iata, todo)
    lastservice1 = todo
        
    
    servicesfile_edg = cf.data_dir + 'routes-utf8-small.csv'
    input_file_edg = csv.DictReader(open(servicesfile_edg, encoding="utf-8"),
                                delimiter=",")
    
    for service in input_file_edg:
        origin=service["Departure"]
        destination=service["Destination"]
        distance = float(service["distance_km"])
        model.addConnection(catalog,origin,destination,distance)
        model.addConNormal(catalog,origin,destination,distance)
    
    servicesfile_cities = cf.data_dir + "worldcities-utf8.csv"
    input_file_city = csv.DictReader(open(servicesfile_cities, encoding="utf-8"),
                                delimiter=",")
    firstcity = None
    for service in input_file_city:
        if firstcity == None:
            firstcity = service
        ciudadela=service["city_ascii"]
        model.addCity(catalog, ciudadela,service)
    lastcity=service
        
    return firstservice1, lastservice1, firstcity, lastcity

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def getNumVertices(grafo):
    return model.getNumVertices(grafo)

def getNumArcos(grafo):
    return model.getNumArcos(grafo)

def getMapSize(mapa):
    return model.getMapSize(mapa)

def reqUno(catalog):
    return model.reqUno(catalog)

def reqDos(catalog, aereo1, aereo2):
    return model.reqDos(catalog, aereo1, aereo2)

def GetAirport(catalog, aereo):
    return model.GetAirport(catalog, aereo)

def reqCuatro(catalog, origen, millas):
    return model.reqCuatro(catalog, origen, millas)


