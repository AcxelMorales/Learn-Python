from classes.herencia_multiple.color import Color
from classes.herencia_multiple.figura_geo import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        self.lado = lado
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.lado * self.lado
