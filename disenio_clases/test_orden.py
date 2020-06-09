from disenio_clases.producto import Producto
from disenio_clases.orden import Orden


p1 = Producto("Xbox One", 9000.00)
p2 = Producto("Lenovo 3300", 12000.00)
p3 = Producto("Xiaomi redmi 8", 3300.00)

productos1 = [p1, p2, p3]
productos2 = [p1, p3]

o1 = Orden(productos1)
o1.agregar_producto(Producto("Nike air max 2090", 3100))
print(o1)
print("Total: ${}".format(o1.calcular_total()))

o2 = Orden(productos2)
o2.agregar_producto(Producto("Test", 10.50))
print(o2)
print("Total: ${}".format(o2.calcular_total()))
