from Nodo.NodoVecino import Vecino


class ListVecinos():

    def __init__(self):
        self.head = None

    def append(self, nuevoVecino):
        if self.head is None:
            self.head = Vecino(data=nuevoVecino)
        else:
            current = Vecino(data=nuevoVecino, link=self.head)
            self.head.previous = current
            self.head = current

    def recorrerVecino(self):
        if self.head is None:
            return
        current = self.head
        print("Codigo: ", current.data.codigo,
              " Patron: ", current.data.patron)

        while current.link:
            current = current.link
            print("Codigo: ", current.data.codigo,
                  " Patron: ", current.data.patron)

    def busquedaVecino(self, codigo):
        current = self.head

        while current and current.data.codigo != codigo:
            current = current.link

        if current is None:
            print("El Codigo no Existe en el Piso")
            return None
        elif current:
            return current.data

    def eliminarPatron(self, codigo):
        current = self.head
        while current:
            if current.data.codigo == codigo:
                if current.previous:
                    if current.link:
                        current.previous.link = current.link
                        current.link.previous = current.previous
                    else:
                        current.previous.link = None
                        current.previous = None
                else:
                    if current.link:
                        self.head = current.link
                        current.link.previous = None
                        # self.primero.anterior = None
                    else:
                        self.head = None
                return True
            else:
                current = current.link
        return False
