class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def calcular_volumen(self):
        volumen = self.alto * self.ancho * self.largo
        return volumen


alto = float(input("Alto: "))
ancho = float(input("Ancho: "))
largo = float(input("Largo: "))

caja = Caja(alto, ancho, largo)
print("Volumen: {}".format(caja.calcular_volumen()))
