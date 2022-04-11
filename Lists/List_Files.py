from Nodes.Nodo_File import Nodo_File


class List_Files():

    def __init__(self):
        self.head = None

    def insertar(self, newfile):
        if self.head is None:
            self.head = Nodo_File(data=newfile)
            return  # Si cumple la condicion, sale del if y cumple la funcion
        actual = self.head
        while actual.siguiente:  # Devuelve True si el siguiente no es vacio, si es vacio sale del ciclo
            actual = actual.siguiente
        actual.siguiente = Nodo_File(data=newfile)

    def recorrer(self):
        actual = self.head
        while actual != None:
            print("Nombre:", actual.data.nombre, "Ruta:", actual.data.path)
            actual = actual.siguiente

    def eliminar(self, nombre: str):
        # finca es parametro
        actual = self.head
        anterior = None
        # mientras actual no este vacio ejecuta lo que viene a continuación
        while actual and actual.data.nombre != nombre:
            anterior = actual
            actual = actual.siguiente
        # si anterior es vacio
        if anterior is None:
            self.head = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def busqueda(self, path):
        actual = self.head
        while actual is not None:
            if actual.data.path == path:
                return actual.data
            actual = actual.siguiente
        return None

    def busquedaFile(self, nombre):
        if self.head is None:
            return None
        actual = self.head
        while actual is not None:
            if actual.data.nombre == nombre:
                return actual.data
            actual = actual.siguiente
        return None
