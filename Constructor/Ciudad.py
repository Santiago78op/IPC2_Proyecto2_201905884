from Lista.MatrizDispersa import MatrizDispersa
from Lista.SimpleUnitMilitary import SimpleUnitMilitary
from Lista.Robots import Robots

class Ciudad():
    
    def __init__(self, ciudad=None,filas=None,columnas=None) -> None:
        self.ciudad = ciudad
        self.filas = filas
        self.columnas = columnas
        self.list_row = SimpleUnitMilitary()
        self.matrizOrtogonal = MatrizDispersa(0)
        self.robots = Robots()
        
        