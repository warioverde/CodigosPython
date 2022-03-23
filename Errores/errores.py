while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("tu edad es:",edad)
        break
    except:
        print("ingresaste un valor erroneo")
    finally:
        print("Iteracion finalizada")