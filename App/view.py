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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente a los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("0- Salir")


def initCatalog(tipoEstructura):
    """
    Inicializa el catalogo
    """
    return controller.initCatalog(tipoEstructura)


def cargarData(catalog):
    """
    Carga la información en la estructura de datos
    """
    controller.cargarData(catalog)


def printCronoArtists(anioI,anioF,catalog):
    """
    Imprime el resultado de listar cronológicamente los artistas 
    que nacieron en un rango de años
    """
    artistas = controller.ejecutarCronoArtists(anioI,anioF,catalog)
    tamanio = artistas.size()
    for i in range(0,3):
        print("Nombre: "+artistas[i]["DisplayName"])
        print("Año de nacimiento: "+artistas[i]["BeginDate"])
        print("Nacionalidad: "+artistas[i]["Nationality"])
        print("Género: "+artistas[i]["Gender"])
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    for i in range(-3,0):
        print("Nombre: "+artistas[tamanio+i]["DisplayName"])
        print("Año de nacimiento: "+artistas[tamanio+i]["BeginDate"])
        print("Nacionalidad: "+artistas[tamanio+i]["Nationality"])
        print("Género: "+artistas[tamanio+i]["Gender"])




catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipoEstructura = "SINGLE_LINKED"
        tipoLista = int(input("Seleccione el tipo de representación de lista en donde cargar el catálogo, 1 para \"Arreglo\" o 2 para \"Lista Encadenada\": "))
        if tipoLista == 1:
            tipoEstructura = "ARRAY_LIST"
        elif tipoLista == 2:
            tipoEstructura = "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipoEstructura)
        cargarData(catalog)
        sizeArtists = int(lt.size(catalog['artists']))
        sizeArtworks = int(lt.size(catalog['artworks']))
        print('Número de artistas cargados: ' + str(sizeArtists))
        print('Número de obras cargadas: ' + str(sizeArtworks))
        print('Ultimos tres artistas cargados: ')
        """
        i funciona como iterador para obtener los últimos tres elementos de las listas
        """
        i=2
        while i>=0:
            ultArtists = lt.getElement(catalog['artists'],(sizeArtists-i))
            print("-Nombre: "+ultArtists["DisplayName"])
            print("-ID: "+ultArtists["ConstituentID"])
            i-=1
        print('Ultimas tres obras cargadas: ')
        """
        i funciona como iterador para obtener los últimos tres elementos de las listas
        """
        i=2
        while i>=0:
            ultArtworks = lt.getElement(catalog['artworks'],(sizeArtworks-i))
            print("-Título: "+ultArtworks["Title"])
            print("-ID: "+ultArtworks["ObjectID"])
            i-=1
    elif int(inputs[0]) == 2:
        anioI = int(input("Ingrese el año incial del rango: "))
        anioF = int(input("Ingrese el año final del rango: "))
        printCronoArtists(anioI,anioF,catalog)

    elif int(inputs[0]) == 3:
        pass

    else:
        sys.exit(0)
sys.exit(0)
