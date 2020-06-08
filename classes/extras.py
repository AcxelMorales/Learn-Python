class Persona:
    def __init__(self, nombre, edad, *valores, **keys):
        self.nombre = nombre
        self.edad = edad
        self.valores = valores
        self.keys = keys
    
    def desplegar(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Valores (Tupla): {}".format(self.valores))
        print("Keys (Diccionario): {}".format(self.keys))


acxel = Persona("Acxel", 23, "Python", "Node JS", "Deno", dj="DJango", fl="Flask")
acxel.desplegar()
