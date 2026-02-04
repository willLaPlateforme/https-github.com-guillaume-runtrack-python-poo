class Operation:
    def __init__(self, nombre_1=5, nombre_2=15):
        self.nombre_1 = nombre_1
        self.nombre_2 = nombre_2

    def addition(self):
        result = self.nombre_1 + self.nombre_2
        print(result)


op = Operation()
op.addition()
