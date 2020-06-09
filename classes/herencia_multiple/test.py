from classes.herencia_multiple.cuadrado import Cuadrado
from classes.herencia_multiple.triangulo import Triangulo

c = Cuadrado(6, "Verde")
print(c.area())
print(c.get_color())

#Method Resolution Order
print(Cuadrado.mro())

r = Triangulo(2, 4, "Azul")
print(r.area())
print(r.get_color())

#Method Resolution Order
print(Triangulo.mro())
