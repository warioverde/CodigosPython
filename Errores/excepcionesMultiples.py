while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

while True:
    try:
        num1 = int(input("Ingresa tu edad: "))
        print("Su edad es: ")
        break
    except ValueError:
        print("ingrese un numero")