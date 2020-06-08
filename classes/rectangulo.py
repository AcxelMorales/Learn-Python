class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2


base = float(input("Base: "))
altura = float(input("Altura: "))

rectangulo = Rectangulo(base, altura)
print("Area: {}".format(rectangulo.area()))
print("Perimetro: {}".format(rectangulo.perimetro()))
