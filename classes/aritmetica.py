class Aritmetica:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        return self.n1 + self.n2

    def restart(self):
        return self.n1 - self.n2

    def multiplicar(self):
        return self.n1 * self.n2

    def dividir(self):
        return self.n1 / self.n2

aritmetica = Aritmetica(6, 6)

print("Suma: {}".format(aritmetica.sumar()))
print("Resta: {}".format(aritmetica.restart()))
print("Multiplicacion: {}".format(aritmetica.multiplicar()))
print("Division: {}".format(aritmetica.dividir()))
