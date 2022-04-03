from Nodo.NodoEncabezado import Encabezado


class ListaEncabezado():

    def __init__(self, tipo=None) -> None:
        # tipo puede ser columna o fila
        self.tipo = tipo
        self.primero: Encabezado = None
        self.ultimo: Encabezado = None
        self.size = 0

    def appendEncabezado(self, nuevo):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:

            # INSERTAR EN ORDEN (IMPORTANTE)
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                aux = self.primero

                while aux != None:
                    if nuevo.id < aux.id:
                        nuevo.siguiente = aux
                        nuevo.anterior = aux.anterior
                        aux.anterior.siguiente = nuevo
                        aux.anterior = nuevo
                        break
                    elif nuevo.id > aux.id:
                        aux = aux.siguiente
                    else:
                        break

    def mostrarEncabezado(self):
        aux = self.primero
        while aux != None:
            print("Encabezado ", self.tipo, aux.id)
            aux = aux.siguiente

    def getEncabezado(self, id) -> Encabezado:
        aux = self.primero
        while aux != None:
            if id == aux.id:
                return aux
            aux = aux.siguiente
        return None
