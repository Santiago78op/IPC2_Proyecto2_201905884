
from Lists.List_UnitMilitary import List_UnitMilitary
from Lists.List_Unit import List_Unit
from Lists.Matriz_Dispersa import Matriz_Dispersa
from Lists.List_Robot import List_Robot


class City():

    def __init__(self, ciudad, filas, columnas) -> None:
        self.ciudad = ciudad
        self.filas = filas
        self.columnas = columnas
        self.list_row = List_UnitMilitary()
        self.unidades = List_Unit()
        self.matrizOrtogonal = Matriz_Dispersa(0)
        self.robots = List_Robot()
