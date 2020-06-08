class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre: {}, edad: {}".format(self.nombre, str(self.edad))


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + ", sueldo ${}".format(str(self.sueldo))


persona = Persona("Acxel", 23)
print(persona)

empleado = Empleado("Acxel", 23, 12000)
print(empleado)
