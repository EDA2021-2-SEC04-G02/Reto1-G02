﻿"""
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


def initCatalog():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def cargarData(catalog):
    """
    Carga la información en la estructura de datos
    """
    controller.cargarData(catalog)


def printCronoArtists(artistas):
    """
    Imprime el resultado de listar cronológicamente los artistas 
    que nacieron en un rango de años
    """
    tamanio = len(artistas)
    print("Número total de artistas en dicho rango: "+str(tamanio)+"\n")
    for i in range(0,3):
        print("Nombre: "+artistas[i]["Nombre"])
        print("Año de nacimiento: "+artistas[i]["Nacimiento"])
        print("Año de fallecimiento: "+artistas[i]["Fallecimiento"])
        print("Nacionalidad: "+artistas[i]["Nacionalidad"])
        print("Género: "+artistas[i]["Género"])
        print("\n")
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")
    for i in range(-3,0):
        print("Nombre: "+artistas[tamanio+i]["Nombre"])
        print("Año de nacimiento: "+artistas[tamanio+i]["Nacimiento"])
        print("Año de fallecimiento: "+artistas[tamanio+i]["Fallecimiento"])
        print("Nacionalidad: "+artistas[tamanio+i]["Nacionalidad"])
        print("Género: "+artistas[tamanio+i]["Género"])
        print("\n")




def printSortArtworks(ord_artworks):
    """
    Imprime el resultado de listar cronológicamente las obras 
    adquiridas en un rango de fechas
    """
    tamanio = len(ord_artworks[1])
    print("\nNúmero total de obras en el rango cronológico: "+str(tamanio)+"\n")
    print("Número total de obras adquiridas por compra: "+str(ord_artworks[0])+"\n")
    printArtworks(ord_artworks,tamanio)



def printArtworks(ord_artworks, tamanio):
    for i in range(0,3):
        print("Título: "+ord_artworks[1][i]["Título"])
        print("Artista(s): "+ord_artworks[1][i]["Artista(s)"])
        print("Fecha: "+ord_artworks[1][i]["Fecha"])
        print("Fecha de adquisición: "+ord_artworks[1][i]["Fecha de adquisición"])
        print("Medio: "+ord_artworks[1][i]["Medio"])
        print("Dimensiones: "+ord_artworks[1][i]["Dimensiones"])
        print("\n")
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")
    for i in range(-3,0):
        print("Título: "+ord_artworks[1][tamanio+i]["Título"])
        print("Artista(s): "+ord_artworks[1][tamanio+i]["Artista(s)"])
        print("Fecha: "+ord_artworks[1][tamanio+i]["Fecha"])
        print("Fecha de adquisición: "+ord_artworks[1][tamanio+i]["Fecha de adquisición"])
        print("Medio: "+ord_artworks[1][tamanio+i]["Medio"])
        print("Dimensiones: "+ord_artworks[1][tamanio+i]["Dimensiones"])
        print("\n")
        


def printArtworksNacionalidad(result):
    print("\nTOP 10 - Nacionalidades en el MOMA\n")
    print("Nacionalidad : Obras")
    for i in range(0,10): 
        print(result[0]["elements"][i][0]+" : "+str(result[0]["elements"][i][1]))
    print("\nLa nacionalidad con más obras en el MOMA es: ",result[0]["elements"][0][0])
    print("Sus primeras y últimas 3 obras son: \n")
    tamanio = len(result[1])
    printArtworks(result, tamanio)



def printNuevaExpo(result, catalog):
    tamanio = len(result[2])
    print("\nNúmero total de obras a exponer: ")
    print(result[0])
    print("\nÁrea aproximada utilizada en m²: ")
    print(result[1])
    print("\nPrimeras 5 y últimas 5 obras de la lista: \n")
    for i in range(0,5):
        nombres = controller.encontrarNombres(result[2]["elements"][i]["ConstituentID"][1:-1].split(","),catalog)
        print("Título: "+result[2]["elements"][i]["Title"])
        print("Artista(s): "+str(nombres)[1:-1])
        print("Fecha: "+result[2]["elements"][i]["Date"])
        print("Clasificación: "+result[2]["elements"][i]["Classification"])
        print("Medio: "+result[2]["elements"][i]["Medium"])
        print("Dimensiones: "+result[2]["elements"][i]["Dimensions"])
        print("\n")
    print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n")
    for i in range(-5,0):
        nombres = controller.encontrarNombres(result[2]["elements"][tamanio-i]["ConstituentID"][1:-1].split(","),catalog)
        print("Título: "+result[2]["elements"][tamanio-i]["Title"])
        print("Artista(s): "+str(nombres)[1:-1])
        print("Fecha: "+result[2]["elements"][tamanio-i]["Date"])
        print("Clasificación: "+result[2]["elements"][tamanio-i]["Classification"])
        print("Medio: "+result[2]["elements"][tamanio-i]["Medium"])
        print("Dimensiones: "+result[2]["elements"][tamanio-i]["Dimensions"])
        print("\n")
    
    


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        cargarData(catalog)
        sizeArtists = int(lt.size(catalog['artists']))
        sizeArtworks = int(lt.size(catalog['artworks']))
        print('\nNúmero de artistas cargados: ' + str(sizeArtists))
        print('\nNúmero de obras cargadas: ' + str(sizeArtworks))
        print('\nUltimos tres artistas cargados: ')
        """
        i funciona como iterador para obtener los últimos tres elementos de las listas
        """
        i=2
        while i>=0:
            ultArtists = lt.getElement(catalog['artists'],(sizeArtists-i))
            print("-Nombre: "+ultArtists["DisplayName"])
            print("-ID: "+ultArtists["ConstituentID"]+"\n")
            i-=1
        print('Ultimas tres obras cargadas: ')
        """
        i funciona como iterador para obtener los últimos tres elementos de las listas
        """
        i=2
        while i>=0:
            ultArtworks = lt.getElement(catalog['artworks'],(sizeArtworks-i))
            print("-Título: "+ultArtworks["Title"])
            print("-ID: "+ultArtworks["ObjectID"]+"\n")
            i-=1
    
    
    
    elif int(inputs[0]) == 2:

        anioI = int(input("Ingrese el año incial del rango: "))
        anioF = int(input("Ingrese el año final del rango: "))
        result = controller.sortArtists(catalog,anioI,anioF)
        printCronoArtists(result)

        
    
    elif int(inputs[0]) == 3:
        diaI = int(input("Ingrese el día incial del rango: "))
        mesI = int(input("Ingrese el mes incial del rango: "))
        anioI = int(input("Ingrese el año incial del rango: "))
        diaF = int(input("Ingrese el día final del rango: "))
        mesF = int(input("Ingrese el mes final del rango: "))
        anioF = int(input("Ingrese el año final del rango: "))
        result = controller.sortArtworks(catalog, anioI, mesI, diaI, anioF, mesF, diaF)
        printSortArtworks(result)





    elif int(inputs[0]) == 5:

        result = controller.artworksNacionalidad(catalog)
        printArtworksNacionalidad(result)
    


    elif int(inputs[0]) == 7:
        anioI = int(input("Ingrese el año incial del rango: "))
        anioF = int(input("Ingrese el año final del rango: "))
        area = float(input("Ingrese el área disponible en metros cuadrados: "))
        result = controller.nuevaExpo(catalog,anioI,anioF,area)
        printNuevaExpo(result, catalog)


    else:
        sys.exit(0)
sys.exit(0)
