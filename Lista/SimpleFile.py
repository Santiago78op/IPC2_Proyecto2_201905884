from Nodo.NodoFile import NodoSimpleFile

class FileListaSimple():

    def __init__(self,nodecount=0) -> None:
        self.head = None
        self.nodecount = nodecount


    def append(self, nuevoFile):
        if self.head is None:
            self.head = NodoSimpleFile(data=nuevoFile)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleFile(data=nuevoFile)
        self.nodecount = self.nodecount + 1


    def recorrerFile(self):
        current = self.head

        while current != None:
            print("Nombre: ",current.data.nombre," Ruta: ",current.data.ruta)
            current = current.link


    def busquedaFile(self,nombre):
        if self.head is None:
            print("El no existe el Archivo en el Folder!!")
            return
        current = self.head

        while current is not None:
            if current.data.nombre == nombre:
                return current.data
            current = current.link
        print("Item no Encontrado")
        return None


    def bubbleSortFiles(self):
        for i in range(self.nodecount-1):
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt:
                if curr.data.nombre > nxt.data.nombre:
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