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


from DISClib.DataStructures.arraylist import getElement
import config as cf
import datetime as dt
import math
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



# Funciones para agregar informacion al catalogo


def addArtist(catalog, artist):
    # Se adiciona la obra a la lista
    lt.addLast(catalog['artists'], artist)
    
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creacion de datos



# Funciones de consulta


def artworksNacionalidad(catalog):
    nacionalidades = {}
    for a in range(1,lt.size(catalog["artworks"])+1):
        artwork = lt.getElement(catalog["artworks"], a)
        artistas = artwork["ConstituentID"][1:-1].split(",")
        for id in artistas:
            encontro = False
            i = 0
            while not encontro and i < lt.size(catalog["artists"]):
                if lt.getElement(catalog["artists"],i)["ConstituentID"] == str(id).strip():
                    nacionalidad = lt.getElement(catalog["artists"],i)["Nationality"]
                    if nacionalidad == "":
                        nacionalidad = "Nationality unknown"
                    if nacionalidad not in nacionalidades:
                        nacionalidades[nacionalidad] = 1
                    else:
                        nacionalidades[nacionalidad] += 1
                    encontro = True
                i += 1

    lstNacion = lt.newList(datastructure="ARRAY_LIST")

    for nacionalidad in nacionalidades:
        lt.addLast(lstNacion,[nacionalidad, nacionalidades[nacionalidad]])
    ordenada = sm.sort(lstNacion, cmpNacionalidad)
    return ordenada



def infoObrasNacionalidad(nacionalidades, catalog):
    nacion = lt.getElement(nacionalidades,1)[0]
    artworks = []
    for a in range(1,lt.size(catalog["artists"])+1):
        artist = lt.getElement(catalog["artists"],a)
        encontro = False
        i=0
        if artist["Nationality"] == nacion:
            while not encontro and i < lt.size(catalog["artworks"]):
                artistas = lt.getElement(catalog["artworks"],i)["ConstituentID"][1:-1].split(",")
                for artista in artistas:
                    if str(artista).strip() == artist["ConstituentID"]:
                        obra = [(lt.getElement(catalog["artworks"],i)),artistas]
                        artworks = artworks + [obra]
                        encontro = True
                i += 1
    return artworks




def costoTransDept(catalog, dept):
    cantidad = 0
    precio = 0
    peso = 0
    for a in range(1,lt.size(catalog["artworks"])+1):
        artwork = lt.getElement(catalog["artworks"],a)
        if artwork["Department"] == dept:
            precioObra = 0
            lados = 0
            l1 = 1
            l2 = 1
            l3 = 1
            l4 = 1
            if artwork["Weight (kg)"] != "" and  artwork["Weight (kg)"] != "0":
                precioObra = 72*artwork["Weight (kg)"]
            if artwork["Depth (cm)"] != "" and artwork["Depth (cm)"] != "0":
                l1 = float(artwork["Depth (cm)"])/100
                lados += 1
            if artwork["Height (cm)"] != "" and artwork["Height (cm)"] != "0":
                l2 = float(artwork["Height (cm)"])/100
                lados += 1
            if artwork["Length (cm)"] != "" and artwork["Length (cm)"] != "0":
                l3 = float(artwork["Length (cm)"])/100
                lados += 1
            if artwork["Width (cm)"] != "" and ["Width (cm)"] != "0":
                l4 = float(artwork["Width (cm)"])/100
                lados += 1
            if artwork["Diameter (cm)"] != "" and artwork["Diameter (cm)"] != "0" and lados <= 1:
                areaDm = (((((float(artwork["Diameter (cm)"])/2)**2)*math.pi)/10000)*l1*l2*l3*l4)
                if areaDm * 72 > precioObra:
                    precioObra = areaDm*72
            if artwork["Circumference (cm)"] != "" and artwork["Circumference (cm)"] != "0" and lados <= 1:
                areaCrcn = ((((float(artwork["Circumference (cm)"])**2)/(4*math.pi))/10000)*l1*l2*l3*l4)
                if areaCrcn * 72 > precioObra:
                    precioObra = areaCrcn*72
            if lados == 2 or lados == 3:
                areaLados = (l1*l2*l3*l4)
                if areaLados * 72 > precioObra:
                    precioObra = areaLados*72
            if precioObra > 0:
                precio += precioObra
            else:
                precio += 48
            cantidad += 1
            if artwork["ObjectID"] == "23776":
                print(artwork)
                print(precioObra)
    print(cantidad)
    print(precio)
    return None






def nuevaExpo(catalog,anioI,anioF,areaMax):
    cantidad = 0
    area = 0
    expo = lt.newList(datastructure="ARRAY_LIST")
    for a in range(1, lt.size(catalog["artworks"])+1):
        artwork = lt.getElement(catalog["artworks"],a)
        if artwork["Date"] != "" and anioI <= int(artwork["Date"]) and int(artwork["Date"]) <= anioF:
            areaArtwork = 0
            if artwork["Diameter (cm)"] != "":
                areaArtwork = ((float(artwork["Diameter (cm)"])/2)**2)*math.pi
            elif artwork["Circumference (cm)"] != "":
                areaArtwork = (float(artwork["Circumference (cm)"])**2)/(4*math.pi)
            elif artwork["Depth (cm)"] == "":
                lados = 0
                l1 = 1
                l2 = 1
                l3 = 1
                if artwork["Height (cm)"] != "":
                    l1 = float(artwork["Height (cm)"])
                    lados += 1
                if artwork["Length (cm)"] != "":
                    l2 = float(artwork["Length (cm)"])
                    lados += 1
                if artwork["Width (cm)"] != "":
                    l3 = float(artwork["Width (cm)"])
                    lados += 1
                if lados == 2:
                    areaArtwork = l1*l2*l3
            if areaArtwork != 0:
                area += areaArtwork
                cantidad += 1
                lt.addLast(expo, artwork)
        if area/10000 > areaMax:
            area -= areaArtwork
            cantidad -= 1
            lt.removeLast(expo)
            break
    area = round(area/10000,3)
    return cantidad, area, expo



# Funciones utilizadas para comparar elementos dentro de una lista


def cmpArtistByBeginDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'BeginDate' de artist1 es menor que el de artist2
    """
    return (str(artist1["BeginDate"])<str(artist2["BeginDate"])) and str(artist1["BeginDate"] != "0") and str(artist2["BeginDate"] != "0")


def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menor que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return (str(artwork1["DateAcquired"])<str(artwork2["DateAcquired"])) and artwork1["DateAcquired"] != None and artwork2["DateAcquired"] != None


def cmpNacionalidad(nacionalidad1, nacionalidad2):
    return nacionalidad1[1]>nacionalidad2[1]



# Funciones de ordenamiento


def sortArtists(catalog):
    sub_list = catalog['artists'].copy()
    sorted_list = sm.sort(sub_list, cmpArtistByBeginDate)
    return sorted_list


def sortArtworks(catalog):
    sub_list = catalog['artworks'].copy()
    sorted_list = sm.sort(sub_list, cmpArtworkByDateAcquired)
    return sorted_list

