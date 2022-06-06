class Route:
    def __init__(self, origen, destino, distancia):
        self.__origen = origen
        self.__destino = destino
        self.__distancia = distancia

    def get_origen(self):
        return self.__origen

    def set_origen(self, origen):
        self.__origen = origen

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        self.__distancia = distancia

