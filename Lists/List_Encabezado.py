from Nodes.Nodo_Encabezado import Nodo_Encabezado


class Lista_Encabezado():
    def __init__(self, tipo=None):
        self.tipo = tipo
        self.primero: Nodo_Encabezado = None
        self.ultimo: Nodo_Encabezado = None
        self.size = 0

    def insertarEncabezado(self, nuevo):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:

            #INSERTAR EN ORDEN (IMPORTANTE)
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

    def getEncabezado(self, id) -> Nodo_Encabezado:
        aux = self.primero
        while aux != None:
            if id == aux.id:
                return aux
            aux = aux.siguiente
        return None
