from Nodes.Nodo_UnitMilitary import Nodo_UnitMilitary


class List_UnitMilitary():

    def __init__(self, nodecount=0) -> None:
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevaUnit):
        if self.head is None:
            self.head = Nodo_UnitMilitary(data=nuevaUnit)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Nodo_UnitMilitary(data=nuevaUnit)
        self.nodecount = self.nodecount + 1

    def recorrerFilas(self):
        if self.head is None:
            return
        current = self.head

        while current != None:
            print("Capacidad: ", current.data.capacidad, " Filas: ",
                  current.data.fila, " Columnas: ", current.data.columna)
            current = current.link

    def FilasChange(self, fila, columna):
        if self.head is None:
            return None
        current = self.head

        while current is not None:
            if current.data.fila == fila and current.data.columna == columna:
                return current.data.capacidad
            current = current.link
        return None
