
# ! Listas de los Nodos
from Lists.List_Encabezado import Lista_Encabezado
from Lists.List_OpenSet import List_OpenSet
from Lists.List_ClosedSet import List_ClosedSet
from Lists.List_Camino import List_Camino

# ? Nodos
from Nodes.Nodo_Encabezado import Nodo_Encabezado

# Todo: librerias
import os


class Matriz_Dispersa():

    def __init__(self, capa=None):
        self.capa = capa
        self.filas = Lista_Encabezado("LISTAS")
        self.columnas = Lista_Encabezado("COLUMNAS")

    def insertar(self, nodoInterno):
        encabezadoX = self.filas.getEncabezado(nodoInterno.x)
        encabezadoY = self.columnas.getEncabezado(nodoInterno.y)

        if encabezadoX == None:
            encabezadoX = Nodo_Encabezado(nodoInterno.x)
            self.filas.insertarEncabezado(encabezadoX)

        if encabezadoY == None:
            encabezadoY = Nodo_Encabezado(nodoInterno.y)
            self.columnas.insertarEncabezado(encabezadoY)

        if encabezadoX.acceso == None:
            encabezadoX.acceso = nodoInterno
        else:
            # INSERTAR NODO INTERNO EN FILA
            if nodoInterno.y < encabezadoX.acceso.y:
                nodoInterno.derecha = encabezadoX.acceso
                encabezadoX.acceso.izquierda = nodoInterno
                encabezadoX.acceso = nodoInterno
            else:
                aux = encabezadoX.acceso
                while aux != None:
                    if nodoInterno.y < aux.y:
                        nodoInterno.derecha = aux
                        nodoInterno.izquierda = aux.izquierda
                        aux.izquierda.derecha = nodoInterno
                        aux.izquierda = nodoInterno
                        break
                    else:
                        if aux.derecha == None:
                            aux.derecha = nodoInterno
                            nodoInterno.izquierda = aux
                            break
                        else:
                            aux = aux.derecha

        if encabezadoY.acceso == None:
            encabezadoY.acceso = nodoInterno
        else:
            # INSERTAR NODO INTERNO EN COLUMNA
            if nodoInterno.x < encabezadoY.acceso.x:
                nodoInterno.abajo = encabezadoY.acceso
                encabezadoY.acceso.arriba = nodoInterno
                encabezadoY.acceso = nodoInterno
            else:
                aux2 = encabezadoY.acceso
                while aux2 != None:
                    if nodoInterno.x < aux2.x:
                        nodoInterno.abajo = aux2
                        nodoInterno.arriba = aux2.arriba
                        aux2.arriba.abajo = nodoInterno
                        aux2.arriba = nodoInterno
                        break
                    else:
                        if aux2.abajo == None:
                            aux2.abajo = nodoInterno
                            nodoInterno.arriba = aux2
                            break
                        else:
                            aux2 = aux2.abajo

    def graficarDot(self, nombre):
        # -- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: ' + str(self.capa) + '\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(
                x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- apuntamos los nodos F entre ellos
        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- Luego de los nodos encabezados fila, seguimos con las columnas, los nodos tendran el foramto Cn
        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.id)+1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(
                y_columna.id, y_columna.id, str(group))
            y_columna = y_columna.siguiente

        # --- apuntamos los nodos C entre ellos
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id,
                                             y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id,
                                             y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        # --- luego que hemos escrito todos los nodos encabezado, apuntamos el nodo root hacua ellos
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                # if aux2.caracter == '-':
                #    grafo += 'N{}_{}[label=" ",group="{}"];\n'.format(aux2.x, aux2.y, int(aux2.y)+1)
                # el
                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                elif aux2.caracter == 'E':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="green"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                elif aux2.caracter == ' ':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="white"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                elif aux2.caracter.isdigit():
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="red"];\n'.format(
                        aux2.x, aux2.y, 'U', int(aux2.y)+1)
                elif aux2.caracter == 'C':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="blue"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                elif aux2.caracter == 'R':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="gray"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                elif aux2.caracter == 'w':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="yellow"];\n'.format(
                        aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.id};'
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.x, aux2.y)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.x, aux2.y, aux.id)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(
                        aux2.x, aux2.y, aux2.derecha.x, aux2.derecha.y)
                    grafo += 'N{}_{}->N{}_{};\n'.format(
                        aux2.derecha.x, aux2.derecha.y, aux2.x, aux2.y)

                rank += 'N{}_{};'.format(aux2.x, aux2.y)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank+'}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.x, aux2.y)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.x, aux2.y, aux.id)
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(
                        aux2.abajo.x, aux2.abajo.y, aux2.x, aux2.y)
                    grafo += 'N{}_{}->N{}_{};\n'.format(
                        aux2.x, aux2.y, aux2.abajo.x, aux2.abajo.y)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)

    # ? funcion heuristica
    def heuristica(self, a, b):
        x = abs(a.x - b.x)
        y = abs(a.y - b.y)

        dist = x + y

        return dist

    #! borrar contenido de la Lista (en progreso)
    def borrarContenido(self, dato, lista=List_OpenSet):
        longitud = lista.longitud()
        for i in range((longitud+1)-1, 0, -1):
            arr = lista.posicionOpenSet(i)
            if arr == dato:
                lista.eliminar(i)

    # ? funcion casilla
    def insertVecinos(self, filas, columnas):
        # Calcular Vecinos
        for fil in range(1, filas+1):
            for col in range(1, columnas+1):
                # Encabezados
                encabezadoX = self.filas.getEncabezado(fil)
                auxInterno = encabezadoX.acceso
                while auxInterno != None:
                    if auxInterno.x == fil and auxInterno.y == col:
                        if auxInterno.izquierda != None:
                            auxInterno.lista_vecinos.insertar(
                                auxInterno.izquierda)
                        if auxInterno.derecha != None:
                            auxInterno.lista_vecinos.insertar(
                                auxInterno.derecha)
                        if auxInterno.arriba != None:
                            auxInterno.lista_vecinos.insertar(
                                auxInterno.arriba)
                        if auxInterno.abajo != None:
                            auxInterno.lista_vecinos.insertar(auxInterno.abajo)
                    auxInterno = auxInterno.derecha

    # ? inicializa
    def inicializa(self, Fstart, Cstart, Fend, Cend, filas, columnas, OpenSet=List_OpenSet):

        Filastart = Fstart
        Columnastart = Cstart
        Filaend = Fend
        Columnaend = Cend

        encabezadoX = self.filas.getEncabezado(Filastart)
        auxInterno = encabezadoX.acceso

        while auxInterno != None:
            if auxInterno.x == Filastart and auxInterno.y == Columnastart:
                OpenSet.insertar(auxInterno)
            auxInterno = auxInterno.derecha

        encabezadoX = self.filas.getEncabezado(Filaend)
        auxInterno = encabezadoX.acceso

        while auxInterno != None:
            if auxInterno.x == Filaend and auxInterno.y == Columnaend:
                end = auxInterno
                print(auxInterno.caracter)
            auxInterno = auxInterno.derecha

        return end

    # ? algoritmo a ejecutar
    def algoritmoChapinRescue(self, end, OpenSet=List_OpenSet, CloseSet=List_ClosedSet, Camino=List_Camino):
        terminado = False
        # Seguiremos hasta encontrar solución
        while not terminado:
            # seguimos si hay algo en openset
            longitud_OpenSet = OpenSet.longitud()
            if longitud_OpenSet > 0:
                ganador = 1  # indice o posicion en la cola openset

                # evaluamos a openset tien un menor coste/esfuerzo
                longitud = OpenSet.longitud()
                for i in range(1, int(longitud)+1):
                    aux_g = OpenSet.posicionOpenSet(ganador)
                    aux_i = OpenSet.posicionOpenSet(i)
                    if aux_i.f < aux_g.f:
                        ganador = i

                # Analizamos la casilla ganadora
                actual = OpenSet.posicionOpenSet(ganador)
                # si hemos llegado al fina Buscamos el camino de Vuelta
                if actual == end:
                    temporal = actual
                    Camino.insertar(temporal)

                    while temporal.padre != None:
                        temporal = temporal.padre
                        Camino.insertar(temporal)
                    Camino.recorrer()
                    terminado = True

                # si no hemos llegado al final, seguimos
                else:
                    self.borrarContenido(actual, OpenSet)
                    CloseSet.insertar(actual)

                    vecinos = actual.lista_vecinos

                    # Recorro vecinos de mi Ganador
                    longitud_Vecinos = vecinos.longitud()

                    for i in range(1, int(longitud_Vecinos)+1):
                        vecino = vecinos.posicion(i)
                        # si el vecino no esta en closedSet y no es una pared
                        closedSet = CloseSet.buscarCloasedSet(
                            vecino.caracter, vecino.x, vecino.y)

                        if closedSet == None and vecino.caracter != '*' and vecino.caracter != 'R' and not vecino.caracter.isdigit():
                            tempG = actual.g + 1

                            # si el vecino esta en OpenSet y su peso es mayor
                            openSet = OpenSet.buscarOpentSet(
                                vecino.caracter, vecino.x, vecino.y)
                            if openSet != None:
                                if tempG < vecino.g:
                                    vecino.g = tempG  # camino mas corto
                            else:
                                vecino.g = tempG
                                OpenSet.insertar(vecino)

                            # Actulizamos valores
                            vecino.h = self.heuristica(vecino, end)
                            vecino.f = vecino.g + vecino.h

                            # Guardar el padre (anterio) -> donde venimos
                            vecino.padre = actual

            else:
                print("Misión Imposible")
                terminado = True  # el algoritmo terminado

    # ? algoritmo a ejecutar
    def algoritmoChapinFighter(self, end, OpenSet=List_OpenSet, CloseSet=List_ClosedSet, Camino=List_Camino):
        terminado = False
        # Seguiremos hasta encontrar solución
        while not terminado:
            # seguimos si hay algo en openset
            longitud_OpenSet = OpenSet.longitud()
            if longitud_OpenSet > 0:
                ganador = 1  # indice o posicion en la cola openset

                # evaluamos a openset tien un menor coste/esfuerzo
                longitud = OpenSet.longitud()
                for i in range(1, int(longitud)+1):
                    aux_g = OpenSet.posicionOpenSet(ganador)
                    aux_i = OpenSet.posicionOpenSet(i)
                    if aux_i.f < aux_g.f:
                        ganador = i

                # Analizamos la casilla ganadora
                actual = OpenSet.posicionOpenSet(ganador)
                # si hemos llegado al fina Buscamos el camino de Vuelta
                if actual == end:
                    temporal = actual
                    Camino.insertar(temporal)

                    while temporal.padre != None:
                        temporal = temporal.padre
                        Camino.insertar(temporal)
                    Camino.recorrer()
                    terminado = True

                # si no hemos llegado al final, seguimos
                else:
                    self.borrarContenido(actual, OpenSet)
                    CloseSet.insertar(actual)

                    vecinos = actual.lista_vecinos

                    # Recorro vecinos de mi Ganador
                    longitud_Vecinos = vecinos.longitud()

                    for i in range(1, int(longitud_Vecinos)+1):
                        vecino = vecinos.posicion(i)
                        # si el vecino no esta en closedSet y no es una pared
                        closedSet = CloseSet.buscarCloasedSet(
                            vecino.caracter, vecino.x, vecino.y)

                        if vecino.x == end.x and vecino.y == end.y:
                            if closedSet == None and vecino.caracter != '*':
                                tempG = actual.g + 1

                                # si el vecino esta en OpenSet y su peso es mayor
                                openSet = OpenSet.buscarOpentSet(
                                    vecino.caracter, vecino.x, vecino.y)
                                if openSet != None:
                                    if tempG < vecino.g:
                                        vecino.g = tempG  # camino mas corto
                                else:
                                    vecino.g = tempG
                                    OpenSet.insertar(vecino)

                                # Actulizamos valores
                                vecino.h = self.heuristica(vecino, end)
                                vecino.f = vecino.g + vecino.h

                                # Guardar el padre (anterio) -> donde venimos
                                vecino.padre = actual

                        else:
                            if closedSet == None and vecino.caracter != '*' and vecino.caracter != 'R':
                                tempG = actual.g + 1

                                # si el vecino esta en OpenSet y su peso es mayor
                                openSet = OpenSet.buscarOpentSet(
                                    vecino.caracter, vecino.x, vecino.y)
                                if openSet != None:
                                    if tempG < vecino.g:
                                        vecino.g = tempG  # camino mas corto
                                else:
                                    vecino.g = tempG
                                    OpenSet.insertar(vecino)

                                # Actulizamos valores
                                vecino.h = self.heuristica(vecino, end)
                                vecino.f = vecino.g + vecino.h

                                # Guardar el padre (anterio) -> donde venimos
                                vecino.padre = actual

            else:
                print("Misión Imposible")
                terminado = True  # el algoritmo terminado

    def cambiarValores(self, Filas, Columnas, Camino=List_Camino):
        for fil in range(1, Filas+1):
            # Encabezados
            encabezadoX = self.filas.getEncabezado(fil)
            auxInterno = encabezadoX.acceso
            while auxInterno != None:
                longitud = Camino.longitud()
                for way in range((longitud+1)-1, 0, -1):
                    temporal = Camino.posicionCamino(way)
                    if auxInterno.x == temporal.x and auxInterno.y == temporal.y:
                        if auxInterno.caracter == 'R' and temporal.caracter == 'R':
                            auxInterno.caracter = 'R'
                        elif auxInterno.caracter == 'E' and temporal.caracter == 'E':
                            auxInterno.caracter = 'E'
                        elif auxInterno.caracter == 'C' and temporal.caracter == 'C':
                            auxInterno.caracter = 'C'
                        elif auxInterno.caracter.isdigit and temporal.caracter.isdigit():
                            auxInterno.caracter = temporal.caracter
                        elif auxInterno.caracter == ' ' and temporal.caracter == ' ':
                            auxInterno.caracter = 'w'
                auxInterno = auxInterno.derecha

    def changeValors(self, robot, Filas, Columnas, Camino=List_Camino):
        tempo = robot.capacidad
        tempo = int(tempo)
        for fil in range(1, Filas+1):
            # Encabezados
            encabezadoX = self.filas.getEncabezado(fil)
            auxInterno = encabezadoX.acceso
            
            while auxInterno != None:
                longitud = Camino.longitud()
                for way in range((longitud+1)-1, 0, -1):
                    temporal = Camino.posicionCamino(way)
                    if auxInterno.x == temporal.x and auxInterno.y == temporal.y:
                        if auxInterno.caracter == 'R' and temporal.caracter == 'R':
                            auxInterno.caracter = 'R'
                        elif auxInterno.caracter == 'E' and temporal.caracter == 'E':
                            auxInterno.caracter = 'E'
                        elif auxInterno.caracter == 'C' and temporal.caracter == 'C':
                            auxInterno.caracter = 'C'
                        elif auxInterno.caracter.isdigit and temporal.caracter.isdigit():
                            valor = temporal.caracter
                            valor = int(valor)
                            aux = tempo - valor
                            tempo = aux
                            if aux >= 0:
                                continue
                            elif aux < 0:
                                print(
                                    "\nLa Capacidad del robot no es suficiente para la mision")
                                tempo = ''
                            auxInterno.caracter = temporal.caracter
                        elif auxInterno.caracter == ' ' and temporal.caracter == ' ':
                            auxInterno.caracter = 'w'
                auxInterno = auxInterno.derecha
        return tempo

    # ? principal
    def principal(self, Fstart, Cstart, Fend, Cend, Filas, Columnas, robot, ciudad) -> None:
        Fstart = int(Fstart)
        Cstart = int(Cstart)
        Fend = int(Fend)
        Cend = int(Cend)
        Filas = int(Filas)
        Columnas = int(Columnas)
        openSet = List_OpenSet()
        closedSet = List_ClosedSet()
        camino = List_Camino()
        end = self.inicializa(Fstart, Cstart, Fend, Cend,
                              Filas, Columnas, openSet)
        self.insertVecinos(Filas, Columnas)
        if robot.tipo == 'ChapinRescue':
            self.algoritmoChapinRescue(end, openSet, closedSet, camino)
            self.cambiarValores(Filas, Columnas, camino)
            self.graficarDot(ciudad)
            print(
                f'\nEl Robot {robot.robot} logro recorrer todo el camino, su capacidad: {robot.capacidad}')
        elif robot.tipo == 'ChapinFighter':
            self.algoritmoChapinFighter(end, openSet, closedSet, camino)
            tempo = self.changeValors(robot, Filas, Columnas, camino)
            if tempo != '':
                self.graficarDot(ciudad)
                print(
                    f'\nEl Robot {robot.robot} logro recorrer todo el camino, su capacidad: {tempo}')
            elif tempo == '':  
                print(
                    f'\nEl Robot {robot.robot} no logro recorrer todo el camino, su capacidad es menor que cualquier Unidad Militar Evaluada')
