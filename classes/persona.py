class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Persona.nombre = "Acxel"
Persona.edad = 23

persona = Persona("Juan", 34)
print(persona.nombre)
print(id(persona))
