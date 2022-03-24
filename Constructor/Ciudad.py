from Lista.MatrizDispersa import MatrizDispersa
from Lista.Robots import Robots

class Ciudad():
    
    def __init__(self, ciudad=None,filas=None,columnas=None) -> None:
        self.ciudad = ciudad
        self.filas = filas
        self.columnas = columnas
        self.matrizOrtogonal = MatrizDispersa()
        self.robots = Robots()
        
        