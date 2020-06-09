class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1

        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def get_id_producto(self):
        return self.__id_producto

    def __str__(self):
        return "ID: {}, Nombre: {}, Precio: ${}".format(self.__id_producto, self.__nombre, str(self.__precio))
