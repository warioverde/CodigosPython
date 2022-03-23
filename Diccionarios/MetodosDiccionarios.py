diccionario = {1:2, 2:3, 3:4}
diccionario2 = {4:5, 6:7}
print(diccionario)
diccionario.pop(3)
print(diccionario)
#diccionario.clear()
print(diccionario)
print(diccionario.get(1))
diccionario.setdefault(4,"Seba")
print(diccionario)
diccionario.update(diccionario2)
print(diccionario)
print(diccionario2.copy())