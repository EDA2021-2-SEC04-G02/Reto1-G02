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


import config as cf
import datetime as dt
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as sm
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de artistas. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}
    
    catalog['artworks'] = lt.newList(datastructure="ARRAY_LIST")
    catalog['artists'] = lt.newList(datastructure="ARRAY_LIST")

    return catalog


def addArtist(catalog, artist):
    # Se adiciona la obra a la lista
    lt.addLast(catalog['artists'], artist)
    
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista
    lt.addLast(catalog['artworks'], artwork)



# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpArtistByBeginDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'BeginDate' de artist1 es menor que el de artist2
    """
    return (str(artist1["BeginDate"])<str(artist2["BeginDate"])) and str(artist1["BeginDate"] != "0") and str(artist2["BeginDate"] != "0")


def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return (str(artwork1["DateAcquired"])<str(artwork2["DateAcquired"])) and artwork1["DateAcquired"] != None and artwork2["DateAcquired"] != None

# Funciones de ordenamiento


def sortArtists(catalog):
    sub_list = catalog['artists'].copy()
    sorted_list = sm.sort(sub_list, cmpArtistByBeginDate)
    return sorted_list


def sortArtworks(catalog):
    sub_list = catalog['artworks'].copy()
    sorted_list = sm.sort(sub_list, cmpArtworkByDateAcquired)
    return sorted_list
