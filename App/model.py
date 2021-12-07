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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import newList
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import prim as pr
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error

assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador
   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
    """
    try:
        catalog = {
                    'airports': None,
                    'conect_digraph': None,
                    'conect_normgraph': None,
                    'cities': None,
                    'SCC': None
                    }

        catalog['airports'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)
        catalog['cities'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)

        catalog['conect_digraph'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)

        catalog['conect_normgraph'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              comparefunction=compareStopIds)
        return catalog
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# Funciones para agregar informacion al grafo



def addAirport(catalog, stopid, todo):
    """
    Adiciona una estación como un vertice del grafo
    """
    try:
        if not gr.containsVertex(catalog['conect_digraph'], stopid):
            gr.insertVertex(catalog['conect_digraph'], stopid)
        if not mp.contains(catalog["airports"],stopid):
            mp.put(catalog["airports"],stopid,todo)
        
    except Exception as exp:
        error.reraise(exp, 'model:addstop')

def addCity(catalog, stopid, todo):
    """
    Adiciona una estación como un vertice del grafo
    """
    try:
        if not mp.contains(catalog["cities"],stopid):
            city = lt.newList("ARRAY_LIST")
            mp.put(catalog["cities"],stopid,city)
        else:
            city = me.getValue(mp.get(catalog["cities"],stopid))
            
        lt.addLast(city, todo)

    except Exception as exp:
        error.reraise(exp, 'model:addstop')


def addConnection(catalog, origin, destination, distance):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(catalog['conect_digraph'], origin, destination)
    #if edge is None:
    gr.addEdge(catalog['conect_digraph'], origin, destination, distance)
    

def addConNormal(catalog, origin, destination, distance):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(catalog['conect_digraph'], destination, origin)
    if edge != None:
        if not gr.containsVertex(catalog['conect_normgraph'], destination):
            gr.insertVertex(catalog['conect_normgraph'], destination)
        if not gr.containsVertex(catalog['conect_normgraph'], origin):
            gr.insertVertex(catalog['conect_normgraph'], origin)
        edgee = gr.getEdge(catalog['conect_normgraph'], origin, destination)
        if edgee is None:
            gr.addEdge(catalog['conect_normgraph'], origin, destination, distance)
    

# ==============================
# Funciones de consulta
# ==============================

def reqUno(catalog):

    intercon = lt.newList("ARRAY_LIST")
    vertices = gr.vertices(catalog["conect_digraph"])
    ver = lt.iterator(vertices)
    total = 0

    for v in ver:
        inedges = gr.indegree(catalog["conect_digraph"], v)
        outedges =  gr.outdegree(catalog["conect_digraph"], v)
        number = inedges + outedges
        info = me.getValue(mp.get(catalog["airports"], v))
        airp = {'edges': number,
                'IN': inedges,
                'OUT': outedges,
                'airport' : info}
        lt.addLast(intercon, airp)

        if number != 0:
            total +=1

    intercon = sa.sort(intercon, cmpnumedges)

    return intercon, total


def reqDos(catalog, aereo1, aereo2):

    conectados = catalog["SCC"]
    numero = scc.connectedComponents(conectados)
    fuerte = scc.stronglyConnected(conectados, aereo1, aereo2)
    return [numero, fuerte]

def reqCuatro(catalog, origen, millas):

    disponibles  = (float(millas)/2)*1.6
    search = pr.PrimMST(catalog["conect_normgraph"])
    mst = pr.prim(catalog["conect_normgraph"], search, origen)
    return mst


def reqCinco(catalog, cerrar):
    number1 = 0
    afec1 = lt.newList("ARRAY_LIST")
    if gr.containsVertex(catalog["conect_digraph"], cerrar):
        inedges1 = gr.indegree(catalog["conect_digraph"], cerrar)
        outedges1 =  gr.outdegree(catalog["conect_digraph"], cerrar)
        number1 = inedges1 + outedges1

        afectados = lt.iterator(gr.adjacents(catalog["conect_digraph"], cerrar))
        cont1 = lt.newList("ARRAY_LIST")
        
        
        for i in afectados:
            if lt.isPresent(cont1, i) == 0:
                p = me.getValue(mp.get(catalog["airports"], i))
                lt.addLast(cont1, i)
                lt.addLast(afec1, p)

    number2 = 0
    afec2 = lt.newList("ARRAY_LIST")
    if gr.containsVertex(catalog["conect_normgraph"], cerrar):
        number2 = gr.degree(catalog["conect_normgraph"], cerrar)

        afectados2 = lt.iterator(gr.adjacents(catalog["conect_normgraph"], cerrar))
        cont2 = lt.newList("ARRAY_LIST")
        
        
        for i in afectados2:
            if lt.isPresent(cont1, i) == 0:
                p = me.getValue(mp.get(catalog["airports"], i))
                lt.addLast(cont2, i)
                lt.addLast(afec2, p)


    return number1, afec1, number2, afec2, 
    




# ==============================
# Funciones Helper
# ==============================

def conectados(catalog):
    catalog["SCC"] = scc.KosarajuSCC(catalog["conect_digraph"])

def numConecados(catalog):
    return scc.connectedComponents(catalog["SCC"])

def getNumVertices(grafo):
    return gr.numVertices(grafo)

def getNumArcos(grafo):
    return gr.numEdges(grafo)

def getMapSize(mapa):
    datos = mp.valueSet(mapa)
    data = lt.iterator(datos)
    size = 0

    for i in data:
        size += lt.size(i)

    return size

def GetAirport(catalog, aereo):
    aereopuertos = catalog["airports"]
    return me.getValue(mp.get(aereopuertos, aereo))

# ==============================
# Funciones de Comparacion
# ==============================


def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1


def compareroutes(route1, route2):
    """
    Compara dos rutas
    """
    if (route1 == route2):
        return 0
    elif (route1 > route2):
        return 1
    else:
        return -1

def cmpnumedges(edge1, edge2):
    return edge1["edges"]>edge2["edges"]