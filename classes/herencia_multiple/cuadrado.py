from classes.herencia_multiple.color import Color
from classes.herencia_multiple.figura_geo import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        self.__lado = lado
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def get_lado(self):
        return self.__lado

    def set_lado(self, lado):
        self.__lado = lado

    def area(self):
        return self.__lado * self.__lado
