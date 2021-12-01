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


def loadServices(analyzer, servicesfile_vertex, servicesfile_edges,servicesfile_city):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.
    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile_ver = cf.data_dir + servicesfile_vertex
    input_file_ver = csv.DictReader(open(servicesfile_ver, encoding="utf-8"),
                                delimiter=",")
    firstservice=None
    for todo in input_file_ver:
        if firstservice==None:
            firstservice=todo
        iata= todo["IATA"]
        model.addAirport(analyzer, iata, todo)
        
    
    servicesfile_edg = cf.data_dir + servicesfile_edges
    input_file_edg = csv.DictReader(open(servicesfile_edg, encoding="utf-8"),
                                delimiter=",")
    lastservice = None
    for service in input_file_edg:
        origin=service["Departure"]
        destination=service["Destination"]
        distance = float(service["distance_km"])
        model.addConnection(analyzer,origin,destination,distance)
        model.addConNormal(analyzer,origin,destination,distance)
    
    servicesfile_cities = cf.data_dir + servicesfile_city
    input_file_city = csv.DictReader(open(servicesfile_cities, encoding="utf-8"),
                                delimiter=",")
    lastcity = None
    for service in input_file_city:
        ciudadela=service["city_ascii"]
        model.addCity(analyzer, ciudadela,service)
        lastcity=service
        
    #model.addRouteConnections(analyzer)
    return analyzer,firstservice,lastcity

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def totalStopsdi(analyzer):
    """
    Total de paradas de autobus
    """
    return model.totalStopsdi(analyzer)


def totalConnectionsdi(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnectionsdi(analyzer)

def totalStopsno(analyzer):
    """
    Total de paradas de autobus
    """
    return model.totalStopsno(analyzer)


def totalConnectionsno(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnectionsno(analyzer)
def totalciu(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalciu(analyzer)

def connectedComponents(analyzer):
    """
    Numero de componentes fuertemente conectados
    """
    return model.connectedComponents(analyzer)


def minimumCostPaths(analyzer, initialStation):
    """
    Calcula todos los caminos de costo minimo de initialStation a todas
    las otras estaciones del sistema
    """
    return model.minimumCostPaths(analyzer, initialStation)


def hasPath(analyzer, destStation):
    """
    Informa si existe un camino entre initialStation y destStation
    """
    return model.hasPath(analyzer, destStation)


def minimumCostPath(analyzer, destStation):
    """
    Retorna el camino de costo minimo desde initialStation a destStation
    """
    return model.minimumCostPath(analyzer, destStation)


def servedRoutes(analyzer):
    """
    Retorna el camino de costo minimo desde initialStation a destStation
    """
    maxvert, maxdeg = model.servedRoutes(analyzer)
    return maxvert, maxdeg