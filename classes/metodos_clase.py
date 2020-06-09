class MiClase:
    var_clase = "Variable clase"

    def __init__(self):
        self.var_instancia = "Variable instancia"

    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.var_clase)

    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: {}".format(str(cls)))
        print(cls.var_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()

        print(self.var_instancia)
        print(self.var_clase)

MiClase.metodo_estatico()
MiClase.metodo_clase()
print("++++++++++++++++++++++++++++++++++++++++++++++")
o = MiClase()
o.metodo_instancia()
