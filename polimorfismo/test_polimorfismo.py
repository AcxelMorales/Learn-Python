from polimorfismo.empleado import Empleado
from polimorfismo.gerente import Gerente


def imprimir_detalles(obj):
    print(type(obj))
    print(obj, end="\n\n")

    if isinstance(obj, Gerente):
        print(obj.departamento)

empleado = Empleado("Juan", 6000)
imprimir_detalles(empleado)

gerente = Gerente("Acxel", 12000, "Tecnologia")
imprimir_detalles(gerente)

empleado = Gerente("Test", 20000, "Negocio")
imprimir_detalles(empleado)
