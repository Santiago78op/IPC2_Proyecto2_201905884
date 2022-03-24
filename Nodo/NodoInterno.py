
class NodoInterno():
    
    def __init__(self, x=None,y=None,caracter=None) -> None:
        self.caracter = caracter
        self.x = x
        self.y = y
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        