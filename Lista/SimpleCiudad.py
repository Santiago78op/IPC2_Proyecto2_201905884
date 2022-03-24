from Nodo.NodoCiudad import NodoSimpleCiudad

class CiudadListaSimple():

    def __init__(self,nodecount=0):
        self.head = None
        self.nodecount = nodecount


    def append(self, nuevaCiudad):
        if self.head is None:
            self.head = NodoSimpleCiudad(data=nuevaCiudad)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleCiudad(data=nuevaCiudad)
        self.nodecount = self.nodecount + 1


    def recorrerCiudad(self):
        current = self.head

        while current != None:
            print("Ciudad: ",current.data.ciudad," Filas: ",current.data.filas," Columnas: ",current.data.columnas)
            current = current.link


    def busquedaCiudad(self,ciudad):
        if self.head is None:
            print("El no existe el Archivo en el Folder!!")
            return
        current = self.head

        while current is not None:
            if current.data.ciudad == ciudad:
                return current.data
            current = current.link
        print("Item no Encontrado")
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
                    prev=curr
                    curr=nxt
                    nxt=nxt.link
            i=i+1