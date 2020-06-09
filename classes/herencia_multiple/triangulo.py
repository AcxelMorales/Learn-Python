from classes.herencia_multiple.color import Color
from classes.herencia_multiple.figura_geo import FiguraGeometrica


class Triangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        self.__base = base
        self.__altura = altura
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def area(self):
        return (self.__base * self.__altura) / 2
