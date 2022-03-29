from Nodo.NodoUnitMilitary import NodoSimpleUnitMilitary


class SimpleUnitMilitary():

    def __init__(self, nodecount=0):
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevaUnit):
        if self.head is None:
            self.head = NodoSimpleUnitMilitary(data=nuevaUnit)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleUnitMilitary(data=nuevaUnit)
        self.nodecount = self.nodecount + 1

    def recorrerFilas(self):
        current = self.head

        while current != None:
            print("Capacidad: ", current.data.capacidad, " Filas: ",
                  current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def FilasChange(self, fila, columna):
        if self.head is None:
            print("El no existe el Archivo en el Folder!!")
            return
        current = self.head

        while current is not None:
            if current.data.fila == fila and current.data.columna == columna:
                return current.data.capacidad
            current = current.link
        return None
