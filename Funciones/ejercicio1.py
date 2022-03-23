lista = []
def pedirNumeros():
    agregarNumero = True
    while(agregarNumero):
        numero = int(input("Ingrese numero "))
        lista.append(numero)
        print("Desea agregar otro numero?")
        print("1.-Si")
        print("2.-No")
        respuesta = int(input(" "))
        if(respuesta == 1):
            pass
        else:
            break
def ordenarNum():
    lista.sort()
    listaPar = []
    listaImpar = []
    for i in lista:
        if i % 2 == 0:
            listaPar.append(i)
        else:
            listaImpar.append(i)
    print(listaPar)
    print(listaImpar)

pedirNumeros()
ordenarNum()
    
