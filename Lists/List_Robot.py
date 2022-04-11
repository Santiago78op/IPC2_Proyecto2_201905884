from Nodes.Nodo_Robot import Nodo_Robot


class List_Robot():

    def __init__(self, nodecount=0) -> None:
        self.head = None
        self.nodecount = nodecount

    def append(self, nuevoRobot):
        if self.head is None:
            self.head = Nodo_Robot(data=nuevoRobot)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Nodo_Robot(data=nuevoRobot)
        self.nodecount = self.nodecount + 1

    def recorrerRobots(self):
        if self.head is None:
            return None
        current = self.head

        while current != None:
            print("Robot: ", current.data.robot, " Tipo: ",
                  current.data.tipo, " Capcidad: ", current.data.capacidad)
            current = current.link

    def chapinRescue(self):
        current = self.head

        while current != None:
            if current.data.tipo == 'ChapinRescue':
                print("Robot: ", current.data.robot, " Tipo: ",
                      current.data.tipo, " Capcidad: ", current.data.capacidad)
            current = current.link

    def chapinFighter(self):
        current = self.head

        while current != None:
            if current.data.tipo == 'ChapinFighter':
                print("Robot: ", current.data.robot, " Tipo: ",
                      current.data.tipo, " Capcidad: ", current.data.capacidad)
            current = current.link

    def busquedaRobot(self, robot):
        if self.head is None:
            return None
        current = self.head

        while current is not None:
            if current.data.robot == robot:
                return current.data
            current = current.link
        return None

    def busquedaRobots(self, tipo):
        current = self.head

        cont = 0
        while current != None:
            if current.data.tipo == tipo:
                aux = current.data
            cont += 1
            current = current.link
        if cont == 1:
            return cont
        elif cont > 1:
            return cont
        elif cont == 0:
            return cont

    def entregarRobot(self, tipo):
        if self.head is None:
            return
        current = self.head

        while current is not None:
            if current.data.tipo == tipo:
                return current.data
            current = current.link

    def eliminar(self, robot):
        current = self.head
        after = None
        while current and current.data.robot != robot.robot:
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
