from Nodes.Nodo_OpenSet import Nodo_OpenSet


class List_OpenSet():

    def __init__(self):
        self.head = None

    def insertar(self, openSet):
        if self.head is None:
            self.head = Nodo_OpenSet(elemento=openSet)
            return  # Si cumple la condicion, sale del if y cumple la funcion
        actual = self.head
        while actual.siguiente:  # Devuelve True si el siguiente no es vacio, si es vacio sale del ciclo
            actual = actual.siguiente
        actual.siguiente = Nodo_OpenSet(elemento=openSet)

    def recorrer(self):
        actual = self.head
        while actual != None:
            print("Tipo: ", actual.elemento.caracter, " Fila: ",
                  actual.elemento.x, " Columna: ", actual.elemento.y)
            actual = actual.siguiente

    def longitud(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador+1
            actual = actual.siguiente
        return contador

    def posicionOpenSet(self, posicion):
        actual = self.head
        contador = 1
        while actual != None:
            if posicion == contador:
                return actual.elemento
            else:
                actual = actual.siguiente
                contador = contador+1
        return None

    def eliminar(self, posicion):
        actual = self.head
        anterior = None
        contador = 1
        while actual and posicion != contador:
            anterior = actual
            actual = actual.siguiente
            contador = contador+1
        if anterior is None:
            self.head = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def buscarOpentSet(self, tipo, fila, columna):
        actual = self.head
        while actual != None:
            if actual.elemento.caracter == tipo and actual.elemento.x == fila and actual.elemento.y == columna:
                return actual
            else:
                actual = actual.siguiente
        return None
