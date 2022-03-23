import math


a = int(input("ingrese a: "))
b = int(input("ingrese b "))
c = int(input("ingrese c "))
formula1 = ((-b + math.sqrt(b**2 - 4*a*c)) / (2*a))
formula2 = ((-b - math.sqrt(b**2 - 4*a*c)) / (2*a))
print("sus solucioones son:",formula1,"y",formula2)