# directorios internos

# ? Constructores
from Builder.Files import File
from Builder.City import City
from Builder.UnitMilitary import UnitMilitary
from Builder.Unit import Unit
from Builder.Robot import Robot

# TODO: Listas de listas
from Lists.List_Files import List_Files
from Lists.List_City import List_City

# * Nodos
from Nodes.Nodo_Interno import Nodo_Interno


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
        self.lista_ciudad = List_City()

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
        lista_files = List_Files()
        while True:

            self.mostrarMenu()

            opcionMenu = input("Insetar el numero de la opción: >> ")

            try:
                opcionMenu = int(opcionMenu)

                if opcionMenu == self.upload:

                    fileChooser = Tk()
                    fileChooser.withdraw()
                    try:
                        route = askopenfilename(
                            title='Selecciona un archivo', filetypes=[('Archivos', '.xml')])
                        fileChooser.destroy()
                        print('Ruta', route)

                        if route == None or route == '':
                            print(Fore.RED, 'No selecciono ningun archivo!')
                        elif route != None or route != '':
                            self.pathFile(route, lista_files)

                    except (OSError, FileNotFoundError):
                        print(f'Imposble encontrar o abrir la ruta <{route}>')
                    except Exception as error:
                        print(f'Un error a ocurrido: <{error}>')

                elif opcionMenu == self.findfile:

                    lista_files.recorrer()
                    nameFile = input("\nInserta el nombre del Archivo: >> ")
                    dataFile = lista_files.busquedaFile(nameFile)

                    if dataFile is None:
                        print(Fore.RED, "Error!, No existe el Archivo")
                    else:
                        print(Fore.LIGHTWHITE_EX,
                              "El Archivo fue encontrado con Exito!!!!!")
                        print("Nombre: ", dataFile.nombre)

                        contenido = self.readContent(dataFile.path)
                        if contenido != '':
                            lista_ciudades = self.createXml(
                                contenido)

                elif opcionMenu == self.city:
                    print(Fore.LIGHTMAGENTA_EX, "Listado de Ciudades en Orden\n")
                    lista_ciudades.bubbleSortCiudad()
                    lista_ciudades.recorrerCiudad()

                    nameCity = input("\nInserta el nombre de la Ciudad: >> ")
                    nameCity = str(nameCity)

                    if nameCity == '':
                        print('Error, no se ha seleccionado ninguna Ciudad')
                    elif nameCity != '':
                        try:
                            city = lista_ciudades.busquedaCiudad(nameCity)
                            city.matrizOrtogonal.graficarDot(nameCity)
                        except:
                            print('Error, no se encontro la Ciudad')
                            return

                elif opcionMenu == self.safeWay:
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
                                self.misionRescue(lista_ciudades)
                            #!TODO: MISION RECURSOS

                            elif opcionSubMenu == self.misionRecursos:
                                self.misionFighter(lista_ciudades)

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

    def pathFile(self, route, list_File: List_Files):
        ruta = list_File.busqueda(route)
        if ruta == None:
            nombre = os.path.basename(route)
            file = File(nombre, route)
            list_File.insertar(file)
        else:
            print(Fore.GREEN, 'Este archivo ya fue Cargado')

    def readContent(self, ruta):
        entrada = ''
        file = open(ruta, 'r')
        for line in file:
            entrada += line
        file.close()
        return entrada

    def createXml(self, contenido):

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

                    findCity = self.lista_ciudad.busquedaCiudad(name)

                    if findCity == None:
                        city = City(name, filas, columnas)
                        self.lista_ciudad.insertar(city)
                    elif findCity.ciudad == name:
                        self.lista_ciudad.eliminar(findCity)
                        city = City(name, filas, columnas)
                        self.lista_ciudad.insertar(city)

                for unitMilitary in ciudad.iter('unidadMilitar'):
                    unit = unitMilitary.text.strip()
                    unit = str(unit)
                    fila = unitMilitary.attrib['fila']
                    fila = int(fila)
                    columna = unitMilitary.attrib['columna']
                    columna = int(columna)
                    newUnit = UnitMilitary(unit, fila, columna)
                    city.list_row.append(newUnit)

                filasF = 1
                for rows in ciudad.iter('fila'):
                    chart = rows.text
                    chart = chart.replace('"', '')

                    chart = str(chart)
                    cont = 0
                    for f in range(int(filasF), int(filasF)+1):
                        for c in range(1, int(columnas)+1):
                            k = chart[cont]
                            point = city.list_row.FilasChange(f, c)
                            if point != None:
                                change = Nodo_Interno(f, c, point)
                                city.matrizOrtogonal.insertar(change)
                                cont += 1
                            elif point == None:
                                change = Nodo_Interno(f, c, k)
                                city.matrizOrtogonal.insertar(change)
                                cont += 1
                                if k == 'E':
                                    nuevaUnidad = Unit('Entrada', k, f, c)
                                    city.unidades.append(nuevaUnidad)
                                elif k == 'C':
                                    nuevaUnidad = Unit('UnidadCivil', k, f, c)
                                    city.unidades.append(nuevaUnidad)
                                elif k == 'R':
                                    nuevaUnidad = Unit('Recurso', k, f, c)
                                    city.unidades.append(nuevaUnidad)
                    filasF += 1

                for robotes in root:
                    for robots in robotes.iter('robot'):
                        for robot in robots.iter('nombre'):
                            nameRobot = robot.text.strip()
                            findRobot = city.robots.busquedaRobot(nameRobot)
                            if findRobot == None:
                                tipo = robot.attrib['tipo']
                                if 'capacidad' in robot.attrib:
                                    capacidad = robot.attrib['capacidad']
                                    robote = Robot(nameRobot, tipo, capacidad)
                                    city.robots.append(robote)

                                else:
                                    capacidad = None
                                    robote = Robot(nameRobot, tipo, capacidad)
                                    city.robots.append(robote)
                            else:
                                city.robots.eliminar(findRobot)
                                tipo = robot.attrib['tipo']
                                if 'capacidad' in robot.attrib:
                                    capacidad = robot.attrib['capacidad']
                                    robote = Robot(nameRobot, tipo, capacidad)
                                    city.robots.append(robote)

                                else:
                                    capacidad = None
                                    robote = Robot(nameRobot, tipo, capacidad)
                                    city.robots.append(robote)

        return self.lista_ciudad

    def misionRescate(self, lista_ciudades=List_City):
        print(Fore.LIGHTMAGENTA_EX,
              "Listado de Ciudades en Orden\n")
        lista_ciudades.bubbleSortCiudad()
        lista_ciudades.recorrerCiudad()
        nameCity = input(
            "\nInserta el nombre de la Ciudad: >> ")
        if nameCity == '':
            print(
                'Error, no se ha seleccionado ninguna Ciudad')
        elif nameCity != '':
            city = lista_ciudades.busquedaCiudad(
                nameCity)

            print(Fore.LIGHTWHITE_EX,
                  'Misión Rescate')
            numCity = city.unidades.busquedaFilas(
                'Entrada')
            if numCity > 1:
                print(Fore.GREEN,
                      'Lista de Entradas en Ciudad')
                city.unidades.recorrerEntrada()
                filaS = input("Ingrese Fila: >> ")
                columnaS = input(
                    "Ingrese Columna: >> ")
            elif numCity == 0:
                print(
                    Fore.RED, 'Error no existen entradas en la Matriz')
            elif numCity == 1:
                print(Fore.GREEN,
                      'Seleccionando entrada....!')
                numCity = city.unidades.entregarCiudad(
                    'Entrada')
                filaS = numCity.fila
                columnaS = numCity.columna

            print(Fore.LIGHTBLUE_EX,
                  '\n Robots')
            numRobot = city.robots.busquedaRobots(
                'ChapinRescue')
            if numRobot > 1:
                print(Fore.GREEN,
                      'Lista de Robots')
                city.robots.chapinRescue()
                nameR = input(
                    "Ingrese nombre: >> ")
                robote = city.robots.busquedaRobot(
                    nameR)
            elif numRobot == 0:
                print(
                    Fore.RED, 'Error no existen robots ChapinRescue')
            elif numRobot == 1:
                print(Fore.GREEN,
                      'Seleccionando Robot....!')
                robote = city.unidades.entregarRobot(
                    'ChapinRescue')

            print(Fore.GREEN,
                  '\nUnidades Civiles')
            numCity = city.unidades.busquedaFilas(
                'UnidadCivil')
            if numCity > 1:
                print(Fore.GREEN,
                      'Lista de Unidades Civiles en la Ciudad')
                city.unidades.recorrerCiviles()
                filaE = input("Ingrese Fila: >> ")
                columnaE = input(
                    "Ingrese Columna: >> ")
                Fe = filaE
                Ce = columnaE
            elif numCity == 0:
                print(
                    Fore.RED, 'Error no existen Unidades Civiles en la Matriz')
            elif numCity == 1:
                print(Fore.GREEN,
                      'Seleccionando Unidad Civil....!')
                numCity = city.unidades.entregarCiudad(
                    'UnidadCivil')
                Fe = numCity.fila
                Ce = numCity.columna

            print(filaS, columnaS, Fe, Ce,
                  city.filas, city.columnas, robote)
            city.matrizOrtogonal.principal(
                filaS, columnaS, Fe, Ce, city.filas, city.columnas, robote, city.ciudad)

    def misionFighter(self, lista_ciudades=List_City):
        print(Fore.LIGHTMAGENTA_EX,
              "Listado de Ciudades en Orden\n")
        lista_ciudades.bubbleSortCiudad()
        lista_ciudades.recorrerCiudad()
        nameCity = input(
            "\nInserta el nombre de la Ciudad: >> ")
        if nameCity == '':
            print(
                'Error, no se ha seleccionado ninguna Ciudad')
        elif nameCity != '':
            city = lista_ciudades.busquedaCiudad(
                nameCity)

        print(Fore.LIGHTWHITE_EX,
              'Misión de Extración de Recursos')
        numCity = city.unidades.busquedaFilas(
            'Entrada')
        if numCity > 1:
            print(Fore.GREEN,
                  'Lista de Entradas en Ciudad')
            city.unidades.recorrerEntrada()
            filaS = input("Ingrese Fila: >> ")
            columnaS = input(
                "Ingrese Columna: >> ")
        elif numCity == 0:
            print(
                Fore.RED, 'Error no existen entradas en la Matriz')
        elif numCity == 1:
            print(Fore.GREEN,
                  'Seleccionando entrada....!')
            numCity = city.unidades.entregarCiudad(
                'Entrada')
            filaS = numCity.fila
            columnaS = numCity.columna

        print(Fore.LIGHTBLUE_EX,
              '\n Robots')
        numRobot = city.robots.busquedaRobots(
            'ChapinFighter')
        if numRobot > 1:
            print(Fore.GREEN,
                  'Lista de Robots')
            city.robots.chapinFighter()
            nameR = input(
                "Ingrese nombre: >> ")
            robote = city.robots.busquedaRobot(
                nameR)
        elif numRobot == 0:
            print(
                Fore.RED, 'Error no existen robots ChapinFighter')
        elif numRobot == 1:
            print(Fore.GREEN,
                  'Seleccionando Robot....!')
            robote = city.unidades.entregarRobot(
                'ChapinFighter')

        print(Fore.GREEN,
              '\nUnidades Recurso')
        numCity = city.unidades.busquedaFilas(
            'Recurso')
        if numCity > 1:
            print(Fore.GREEN,
                  'Lista de Unidades de Recursos en la Ciudad')
            city.unidades.recorrerRecursos()
            Fe = input("Ingrese Fila: >> ")
            Ce = input("Ingrese Columna: >> ")
        elif numCity == 0:
            print(
                Fore.RED, 'Error no existen Unidades Civiles en la Matriz')
        elif numCity == 1:
            print(Fore.GREEN,
                  'Seleccionando Unidad Recurso....!')
            numCity = city.unidades.entregarCiudad(
                'Recurso')
            Fe = numCity.fila
            Ce = numCity.columna

        print(filaS, columnaS, Fe, Ce,
              city.filas, city.columnas, robote)
        city.matrizOrtogonal.principal(
            filaS, columnaS, int(Fe), int(Ce), int(city.filas), int(city.columnas), robote, city.ciudad)
