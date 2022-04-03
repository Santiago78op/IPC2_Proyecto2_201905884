# directorios internos

# ? Constructores
from Constructor.Algoritmo import Algoritmo
from Constructor.Folders import Files
from Constructor.Ciudad import Ciudad
from Constructor.Robot import Robot
from Constructor.Filas import Filas
from Constructor.UnidadMilitar import UnitMilitary
from Nodo.NodoInterno import NodoInterno

# TODO: Listas de listas
from Lista.SimpleFile import FileListaSimple
from Lista.SimpleCiudad import CiudadListaSimple

# ! librerias externas
import xml.etree.ElementTree as ET
import os
from colorama import Fore
from tkinter import *
from tkinter.filedialog import askopenfilename


class Menu():

    def __init__(self):
        self.upload = 1
        self.findfile = 2
        self.city = 3
        self.safeWay = 4
        self.salir = 0
        self.misionRescate = 1
        self.misionRecursos = 2
        self.lista_ciudades = CiudadListaSimple()

    def mostrarMenu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')
        print(Fore.CYAN, f'''\t<-- Menu Principal Chapín Warriors, S.A. -->\n
Seleccione una Opción:\n
       \t{self.upload}) -> Cargar Archivo
       \t{self.findfile}) -> Buscar Archivo
       \t{self.city}) -> Graficar Ciudad
       \t{self.safeWay}) -> Seleccione Misión
       \t{self.salir}) -> Salir\n''')

    def menu(self) -> bool:
        lista_rutas = list()
        while True:

            self.mostrarMenu()

            opcionMenu = input("Insetar el numero de la opción: >> ")

            try:
                opcionMenu = int(opcionMenu)

                if opcionMenu == self.upload:

                    fileChooser = Tk()
                    fileChooser.withdraw()
                    try:
                        self.route = askopenfilename(
                            title='Selecciona un archivo', filetypes=[('Archivos', '.xml')])
                        fileChooser.destroy()
                        print(self.route)

                        if self.route == '' or self.route == None:
                            print('Error, no se ha seleccionado ningun archivo')
                        else:
                            lista_rutas.append(self.route)

                    except:
                        print('Error, no se ha seleccionado ningun archivo')
                        return
                elif opcionMenu == self.findfile:

                    lista_files = self.readFolder(lista_rutas)
                    lista_files.recorrerFile()
                    nameFile = input("\nInserta el nombre del Archivo: >> ")
                    dataFile = lista_files.busquedaFile(nameFile)

                    if dataFile is None:
                        print(Fore.RED, "No Existe el File Error!")
                    else:
                        print(Fore.LIGHTWHITE_EX,
                              "El File fue encontrado con Exito!!!!!")
                        print("Nombre: ", dataFile.nombre,
                              " Ruta: ", dataFile.ruta)

                        contenido = self.readContent(dataFile.ruta)
                        if contenido != '':
                            lista_ciudades = self.clonFile(contenido)

                elif opcionMenu == self.city:
                    print(Fore.LIGHTMAGENTA_EX, "Listado de Ciudades en Orden\n")
                    lista_ciudades.bubbleSortCiudad()
                    lista_ciudades.recorrerCiudad()

                    nameCity = input("\nInserta el nombre de la Ciudad: >> ")
                    nameCity = str(nameCity)

                    if nameCity == None:
                        print('Error, no se ha seleccionado ninguna Ciudad')
                    elif nameCity != None:
                        try:
                            city = lista_ciudades.busquedaCiudad(nameCity)
                            city.algorithm.recorrer()
                            city.matrizOrtogonal.graficarDot(nameCity)
                        except:
                            print('Error, no se encontro la Ciudad')
                            return

                elif opcionMenu == self.safeWay:
                    print(Fore.LIGHTMAGENTA_EX, "Listado de Ciudades en Orden\n")
                    lista_ciudades.bubbleSortCiudad()
                    lista_ciudades.recorrerCiudad()

                    nameCity = input("\nInserta el nombre de la Ciudad: >> ")
                    nameCity = str(nameCity)

                    if nameCity == None:
                        print('Error, no se ha seleccionado ninguna Ciudad')
                    elif nameCity != None:
                        try:
                            city = lista_ciudades.busquedaCiudad(nameCity)
                            while True:
                                os.system('cls')
                                print(Fore.CYAN, f'''
                            \t<-- Menu Principal Chapín Warriors, S.A. -->\n
    Seleccione una Misión:\n
        \t{self.misionRescate}) -> Misión de rescate
        \t{self.misionRecursos}) -> Misión de extracción de recursos
        \t{self.salir}) -> Salir\n''')

                                opcionSubMenu = input(
                                    "Insetar el numero de la opción: >> ")

                                try:
                                    opcionSubMenu = int(opcionSubMenu)
                                    
                                    #!TODO: MISION RESCATE
                                
                                    if opcionSubMenu == self.misionRescate:
                                        numCity = city.unidades.busquedaFilas(
                                            'Entrada')
                                        if numCity > 1:
                                            city.unidades.recorrerEntrada()
                                            filaE = input("Ingrese Fila: >> ")
                                            columnaE = input(
                                                "Ingrese Columna: >> ")
                                            starPoint = f'{filaE},{columnaE}'
                                        elif numCity == 0:
                                            print(
                                                Fore.RED, 'Error no existen entradas en la Matriz')
                                        elif numCity == 1:
                                            numCity = city.unidades.entregarCiudad(
                                                'Entrada')
                                            filaU = numCity.fila
                                            columnaU = numCity.columna
                                            starPoint = f'{filaU},{columnaU}'
                                            print(starPoint)
                                        
                                        numRobot = city.robots.busquedaRobots(
                                            'ChapinRescue')
                                        if numRobot > 1:
                                            city.robots.chapinRescue()
                                            nameR = input("Ingrese nombre: >> ")
                                            robotR = f'{nameR}'
                                        elif numRobot == 0:
                                            print(
                                                Fore.RED, 'Error no existen robots ChapinRescue')
                                        elif numRobot == 1:
                                            numRobot = city.unidades.entregarRobot(
                                                'ChapinRescue')
                                            nameR = numRobot.robot
                                            robotR = f'{nameR}'
                                            print(robotR)
                                            
                                        numCity = city.unidades.busquedaFilas(
                                            'UnidadCivil')
                                        if numCity > 1:
                                            city.unidades.recorrerCiviles()
                                            filaE = input("Ingrese Fila: >> ")
                                            columnaE = input(
                                                "Ingrese Columna: >> ")
                                            endPoint = f'{filaE},{columnaE}'
                                        elif numCity == 0:
                                            print(
                                                Fore.RED, 'Error no existen Unidades Civiles en la Matriz')
                                        elif numCity == 1:
                                            numCity = city.unidades.entregarCiudad(
                                                'UnidadCivil')
                                            filaU = numCity.fila
                                            columnaU = numCity.columna
                                            endPoint = f'{filaU},{columnaU}'
                                            print(endPoint)
                                                       
                                    #!TODO: MISION RECURSOS

                                    elif opcionSubMenu == self.misionRecursos:
                                        numCity = city.unidades.busquedaFilas(
                                            'Entrada')
                                        if numCity > 1:
                                            city.unidades.recorrerEntrada()
                                            filaE = input("Ingrese Fila: >> ")
                                            columnaE = input(
                                                "Ingrese Columna: >> ")
                                            starPoint = f'{filaE},{columnaE}'
                                        elif numCity == 0:
                                            print(
                                                Fore.RED, 'Error no existen entradas en la Matriz')
                                        elif numCity == 1:
                                            numCity = city.unidades.entregarCiudad(
                                                'Entrada')
                                            filaU = numCity.fila
                                            columnaU = numCity.columna
                                            starPoint = f'{filaU},{columnaU}'
                                            print(starPoint)
                                            
                                        numRobot = city.robots.busquedaRobots(
                                            'ChapinFighter')
                                        if numRobot > 1:
                                            city.robots.chapinFighter()
                                            nameR = input(
                                                "Ingrese nombre: >> ")
                                            robotR = f'{nameR}'
                                        elif numRobot == 0:
                                            print(
                                                Fore.RED, 'Error no existen robots ChapinFighter')
                                        elif numRobot == 1:
                                            numRobot = city.unidades.entregarRobot(
                                                'ChapinFighter')
                                            nameR = numRobot.robot
                                            robotR = f'{nameR}'
                                            print(robotR)

                                        numCity = city.unidades.busquedaFilas(
                                            'Recurso')
                                        if numCity > 1:
                                            city.unidades.recorrerRecursos()
                                            filaE = input("Ingrese Fila: >> ")
                                            columnaE = input(
                                                "Ingrese Columna: >> ")
                                            endPoint = f'{filaE},{columnaE}'
                                        elif numCity == 0:
                                            print(
                                                Fore.RED, 'Error no existen Unidades Civiles en la Matriz')
                                        elif numCity == 1:
                                            numCity = city.unidades.entregarCiudad(
                                                'Recurso')
                                            filaU = numCity.fila
                                            columnaU = numCity.columna
                                            endPoint = f'{filaU},{columnaU}'
                                            print(endPoint)
                                            
                                            
                                    elif opcionSubMenu == self.salir:
                                        print(Fore.GREEN,
                                              "\nSalio del SubMenu Selccionar Mision\n")
                                        False
                                        break
                                    else:
                                        print(Fore.YELLOW,
                                              'Opcion no válida...')
                                    input(
                                        '\nPresiona enter para Ingresar al SubMenú...')
                                    os.system('cls')

                                except ValueError as error:
                                    print(Fore.RED, f'Error: {error}')
                                    print(
                                        Fore.RED, 'El programa no permite carateres tipo alpha')
                                    input(
                                        'Presione la tecla Enter para continuar@')
                        except:
                            print('Error, no se encontro la Ciudad')
                            return

                elif opcionMenu == self.salir:
                    print(Fore.GREEN,
                          "\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW, 'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                print(Fore.RED, f'Error: {error}')
                print(Fore.RED, 'El programa no permite carateres tipo alpha')
                input('Presione la tecla Enter para continuar@')

    def readFolder(self, lista_rutas):
        lista_files = FileListaSimple()
        cont = 1
        for ruta in lista_rutas:
            name = 'Archivo_{}'.format(cont)
            newFile = Files(name, ruta)
            lista_files.append(newFile)
            cont += 1

        return lista_files

    def readContent(self, ruta):
        entrada = ''
        file = open(ruta, 'r')
        for line in file:
            entrada += line
        file.close()
        return entrada

    def clonFile(self, contenido):

        path = 'Data\contenedor.xml'
        with open(path, 'w') as f:
            for line in contenido:
                f.write(line)

        # Archivo Recien Ingresado
        tree = ET.parse(path)
        root = tree.getroot()

        for ciudades in root:
            for ciudad in ciudades.iter('ciudad'):
                for nombre in ciudad.iter('nombre'):
                    name = nombre.text.strip()
                    filas = nombre.attrib['filas']
                    columnas = nombre.attrib['columnas']
                    findCiudad = self.lista_ciudades.busquedaCiudad(name)

                    if findCiudad == None:
                        newCity = Ciudad(name, filas, columnas)
                        self.lista_ciudades.append(newCity)
                    elif findCiudad.ciudad == name:
                        self.lista_ciudades.eliminar(name)
                        newCity = Ciudad(name, filas, columnas)
                        self.lista_ciudades.append(newCity)

                for unitMilitary in ciudad.iter('unidadMilitar'):
                    unit = unitMilitary.text.strip()
                    unit = str(unit)
                    fila = unitMilitary.attrib['fila']
                    fila = int(fila)
                    columna = unitMilitary.attrib['columna']
                    columna = int(columna)
                    newUnit = UnitMilitary(unit, fila, columna)
                    newCity.list_row.append(newUnit)

                filasF = 1
                for rows in ciudad.iter('fila'):
                    chart = rows.text
                    chart = chart.replace('"', '')

                    chart = str(chart)
                    cont = 0
                    for f in range(int(filasF), int(filasF)+1):
                        for c in range(1, int(columnas)+1):
                            k = chart[cont]
                            point = newCity.list_row.FilasChange(f, c)
                            if point != None:
                                change = NodoInterno(f, c, point)
                                newCity.matrizOrtogonal.appendMatriz(change)
                                cont += 1
                            elif point == None:
                                change = NodoInterno(f, c, k)
                                newCity.matrizOrtogonal.appendMatriz(change)
                                cont += 1
                                if k == 'E':
                                    nuevaUnidad = Filas('Entrada', k, f, c)
                                    newCity.unidades.append(nuevaUnidad)
                                elif k == 'C':
                                    nuevaUnidad = Filas('UnidadCivil', k, f, c)
                                    newCity.unidades.append(nuevaUnidad)
                                elif k == 'R':
                                    nuevaUnidad = Filas('Recurso', k, f, c)
                                    newCity.unidades.append(nuevaUnidad)
                    filasF += 1

            for robots in ciudades.iter('robot'):
                for robot in robots.iter('nombre'):
                    nameRobot = robot.text.strip()
                    findRobot = newCity.robots.busquedaRobots(nameRobot)
                    if findRobot == None:
                        tipo = robot.attrib['tipo']
                        if 'capacidad' in robot.attrib:
                            capacidad = robot.attrib['capacidad']
                            robote = Robot(nameRobot, tipo, capacidad)
                            newCity.robots.append(robote)

                        else:
                            capacidad = None
                            robote = Robot(nameRobot, tipo, capacidad)
                            newCity.robots.append(robote)
                    else:
                        newCity.robots.eliminar(nameRobot)
                        tipo = robot.attrib['tipo']
                        if 'capacidad' in robot.attrib:
                            capacidad = robot.attrib['capacidad']
                            robote = Robot(nameRobot, tipo, capacidad)
                            newCity.robots.append(robote)

                        else:
                            capacidad = None
                            robote = Robot(nameRobot, tipo, capacidad)
                            newCity.robots.append(robote)

        return self.lista_ciudades
