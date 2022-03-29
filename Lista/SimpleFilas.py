
from Nodo.NodoFilas import NodoSimpleFilas


class FilasListaSimple():

    def __init__(self, nodecount=0):
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevaFila):
        if self.head is None:
            self.head = NodoSimpleFilas(data=nuevaFila)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleFilas(data=nuevaFila)
        self.nodecount = self.nodecount + 1

    def recorrerFilas(self):
        current = self.head

        while current != None:
            print("Caracter: ", current.data.caracter, " Filas: ",
                  current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def FilasChange(self, caracter, fila, columna):
        current = self.head

        if self.head == None:
            return None

        while current != None:
            if current.data.fila == fila and current.data.columna == columna:
                current.data.caracter == caracter
                return current.data
            current = current.link
