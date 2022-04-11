class Nodo_Encabezado():

    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None  # APUNTADOR A NODOS INTERNOS
