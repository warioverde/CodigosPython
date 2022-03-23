class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = float(nota)
    def imprimirNotas(self):
        if self._nota < 4.0:
            print("{} usted tiene un {} y esta reprobado".format(self._nombre,self._nota))
        else:
            print("{} usted tiene un {} y esta aprobado".format(self._nombre,self._nota))

sebastian = Estudiante("Sebastian", 4.0)
sebastian.imprimirNotas()

joaquin = Estudiante("Joaquin", 3.94)
joaquin.imprimirNotas()