class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return "Nombre: {}, Sueldo: ${}".format(self.nombre, str(self.sueldo))
