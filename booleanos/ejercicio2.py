numero = int(input("ingrese numero "))

if (numero < 0):
    numeroTransformado = -numero
    print("su numero en valor absoluto es",numeroTransformado)
elif (numero == 0):
    print("su numero en valor absoluto es",numero)
else:
    print("su numero ya esta en valor absoluto y es {}".format(numero))