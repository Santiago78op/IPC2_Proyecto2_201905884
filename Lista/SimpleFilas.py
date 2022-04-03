
from Nodo.NodoFilas import NodoSimpleFilas


class FilasListaSimple():

    def __init__(self, nodecount=0) -> None:
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevaUnidad):
        if self.head is None:
            self.head = NodoSimpleFilas(data=nuevaUnidad)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleFilas(data=nuevaUnidad)
        self.nodecount = self.nodecount + 1

    def recorrerCiviles(self):
        current = self.head

        while current != None:
            if current.data.unidad == 'UnidadCivil':
                print("Unidad: ", current.data.unidad, "Caracter: ", current.data.caracter, " Filas: ",
                      current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def recorrerRecursos(self):
        current = self.head

        while current != None:
            if current.data.unidad == 'Recurso':
                print("Unidad: ", current.data.unidad, "Caracter: ", current.data.caracter, " Filas: ",
                      current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def recorrerEntrada(self):
        current = self.head

        while current != None:
            if current.data.unidad == 'Entrada':
                print("Entrada: ", current.data.unidad, "Caracter: ", current.data.caracter, " Filas: ",
                      current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def busquedaFilas(self, unidad):
        if self.head is None:
            return
        current = self.head

        cont = 0
        aux = ''
        cadena = ''
        while current is not None:
            if current.data.unidad == unidad:
                aux = current.data
                cont += 1
            current = current.link
        if cont == 1:
            return cont
        elif cont > 1:
            return cont 
        elif cont == 0:
            return cont
    
    def entregarCiudad(self, unidad):
        if self.head is None:
            return
        current = self.head

        while current is not None:
            if current.data.unidad == unidad:
                return current.data
            current = current.link
            
            