class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1

        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    def agregar_producto(self, producto):
        self.__productos.append(producto)
        print("++++++ Agregado ++++++. Orden: {}".format(Orden.contador_ordenes))

    def calcular_total(self):
        total = 0

        for i in self.__productos:
            total += i.get_precio()

        return total

    def __str__(self):
        producto_str = ""

        for i in self.__productos:
            producto_str += i.__str__() + " | "

        return "Orden: {}. Productos: {}".format(self.__id_orden, producto_str)
