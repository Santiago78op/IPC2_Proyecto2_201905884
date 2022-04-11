from Nodes.Nodo_ClosedSet import Nodo_ClosedSet


class List_ClosedSet():

    def __init__(self):
        self.head = None

    def insertar(self, closedSet):
        if self.head is None:
            self.head = Nodo_ClosedSet(elemento=closedSet)
            return  # Si cumple la condicion, sale del if y cumple la funcion
        actual = self.head
        while actual.siguiente:  # Devuelve True si el siguiente no es vacio, si es vacio sale del ciclo
            actual = actual.siguiente
        actual.siguiente = Nodo_ClosedSet(elemento=closedSet)

    def recorrer(self):
        actual = self.head
        while actual != None:
            print("Tipo: ", actual.elemento.elemento.caracter, " Fila: ",
                  actual.elemento.elemento.x, " Columna: ", actual.elemento.elemento.y)
            actual = actual.siguiente

    def longitud(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador+1
            actual = actual.siguiente
        return contador

    def posicionCloasedSet(self, posicion):
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

    def buscarCloasedSet(self, tipo, fila, columna):
        if self.head is None:
            return None
        actual = self.head
        while actual is not None:
            if actual.elemento.caracter == tipo and actual.elemento.x == fila and actual.elemento.y == columna:
                return actual.elemento
            actual = actual.siguiente
        return None
