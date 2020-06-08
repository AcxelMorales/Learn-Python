class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

persona = Persona("Juan")
print(persona.get_nombre())

persona.set_nombre("Pedro")
print(persona.get_nombre())
