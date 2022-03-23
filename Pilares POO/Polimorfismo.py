class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guauu!")
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guau!")
perro.hablar()

animal = Animales("miuau")
animal.hablar()

pez = Pez("Nada")
pez.hablar()