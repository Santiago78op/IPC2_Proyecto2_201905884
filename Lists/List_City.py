from Nodes.Nodo_City import Nodo_City


class List_City():

    def __init__(self, nodecount=0):
        self.head = None
        self.nodecount = nodecount

    def insertar(self, newCity):
        if self.head is None:
            self.head = Nodo_City(data=newCity)
            self.nodecount = self.nodecount + 1
            return  # Si cumple la condicion, sale del if y cumple la funcion
        actual = self.head
        while actual.link:  # Devuelve True si el siguiente no es vacio, si es vacio sale del ciclo
            actual = actual.link
        actual.link = Nodo_City(data=newCity)
        self.nodecount = self.nodecount + 1

    def recorrerCiudad(self):
        current = self.head

        while current != None:
            print("Ciudad: ", current.data.ciudad, " Filas: ",
                  current.data.filas, " Columnas: ", current.data.columnas)
            current = current.link

    def eliminar(self, nombre):
        # finca es parametro
        actual = self.head
        anterior = None
        # mientras actual no este vacio ejecuta lo que viene a continuación
        while actual and actual.data.ciudad != nombre.ciudad:
            anterior = actual
            actual = actual.link
        # si anterior es vacio
        if anterior is None:
            self.head = actual.link
            actual.link = None
        elif actual:
            anterior.link = actual.link
            actual.link = None

    def busquedaCiudad(self, nombre):
        if self.head is None:
            return None
        actual = self.head
        while actual is not None:
            if actual.data.ciudad == nombre:
                return actual.data
            actual = actual.link
        return None

    def bubbleSortCiudad(self):
        for i in range(self.nodecount-1):
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt:
                if curr.data.ciudad > nxt.data.ciudad:
                    if prev == None:
                        prev = curr.link
                        nxt = nxt.link
                        prev.link = curr
                        curr.link = nxt
                        self.head = prev
                    else:
                        temp = nxt
                        nxt = nxt.link
                        prev.link = curr.link
                        prev = temp
                        temp.link = curr
                        curr.link = nxt
                else:
                    prev = curr
                    curr = nxt
                    nxt = nxt.link
            i = i+1
