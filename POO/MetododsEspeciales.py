class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))
    def __str__(self):
        return self.marca +", "+ self.color
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))
telefono = FabricaTelefonos("Nokia","negro")
print(telefono.marca)
print(telefono)