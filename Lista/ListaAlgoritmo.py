from Constructor.Algoritmo import Algoritmo


class AlgoritmoSimple():

    def __init__(self) -> None:
        self.head = Algoritmo()
        self.ultimo = self.head

    def append(self, nuevoALG):
        if self.head.caracter is None:
            self.head = nuevoALG
        elif self.head.link is None:
            self.head.link = nuevoALG
            self.ultimo = nuevoALG
        else:
            self.ultimo.link = nuevoALG
            self.ultimo = nuevoALG

    def recorrer(self):
        aux = self.head
        while aux != None:
            print("Caracter: ", aux.data.caracter, "Fila: ",
                  aux.data.fila, "Columna: ", aux.data.columna)
            aux = aux.link
        print("\n")
