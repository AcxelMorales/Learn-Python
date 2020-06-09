class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __add__(self, other):
        return "{} {}".format(self.__nombre, other.__nombre)

    def __sub__(self, other):
        return "Operacion no soportada"

p1 = Persona("Juan")
p2 = Persona("Francisco")

print(p1 + p2)
print(p1 - p2)
