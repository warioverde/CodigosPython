class Calculadora():
    def __init__(self):
        self.num1 = int(input("ingrese num1 "))
        self.num2 = int(input("ingrese num2 "))
    def sumar(self):
        return self.num1+self.num2
    def restar(self):
        return self.num1-self.num2
    def multiplicar(self):
        return self.num1*self.num2
    def dividir(self):
        if self.num2 == 0:
            return "No se puede dividir por cero"
        else:
            return self.num1/self.num2

while True:
    respuesta = int(input("Quiere hacer un calculo? \n 1.-Si \n 2.-No \n"))
    if respuesta == 1:
        calculadora = Calculadora()
        print("Respuestas",calculadora.sumar(), calculadora.restar(), calculadora.multiplicar(), calculadora.dividir())
    else:
        break