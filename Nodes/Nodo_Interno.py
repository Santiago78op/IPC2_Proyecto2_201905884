from Lists.List_Vecino import List_Vecinos


class Nodo_Interno():
    def __init__(self, x, y, caracter):
        #! Tipo
        self.caracter = caracter
        #! Posición
        self.x = x
        self.y = y
        #! Pesos
        self.f = 0  # ? costo total (g+h)
        self.g = 0  # ? pasos dados
        self.h = 0  # ? heurística (estimación de lo que queda)
        #! Lista Vecinos
        self.lista_vecinos = List_Vecinos()
        #! Padre de la Casilla
        self.padre = None
        #! Punteros
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
