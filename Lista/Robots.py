from Nodo.NodoRobots import NodoSimpleRobots


class Robots():

    def __init__(self, nodecount=0):
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevoRobot):
        if self.head is None:
            self.head = NodoSimpleRobots(data=nuevoRobot)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimpleRobots(data=nuevoRobot)
        self.nodecount = self.nodecount + 1

    def recorrerRobots(self):
        current = self.head

        while current != None:
            print("Robot: ", current.data.robot, " Tipo: ",
                  current.data.tipo, " Capcidad: ", current.data.capacidad)
            current = current.link

    def busquedaRobots(self, robot):
        if self.head is None:
            return
        current = self.head

        while current is not None:
            if current.data.robot == robot:
                return current.data
            current = current.link
        return None

    def eliminar(self, robot: str):
        current = self.head
        after = None
        while current and current.data.robot != robot:
            after = current
            current = current.link
        if after is None:
            self.head = current.link
            current.link = None
        elif current:
            after.link = current.link
            current.link = None

    def bubbleSortRobots(self):
        for i in range(self.nodecount-1):
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt:
                if curr.data.robot > nxt.data.robot:
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
