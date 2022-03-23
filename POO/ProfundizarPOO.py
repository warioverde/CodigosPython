class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel","negro","azul","verde", m1 = 500, m2= 100)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
print(telefono.memoria)

