from abc import ABC, abstractmethod

#ejercico 1
class expresion(ABC):

    @abstractmethod
    def valor(self):
        ...

class Numero(expresion):
    def __init__(self, num) -> None:
        self.num = num

    def valor(self):
        return self.num

class Suma(expresion):
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def valor(self):
        return self.num1.valor() + self.num2.valor()

class Producto(expresion):
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def valor(self):
        return self.num1.valor() * self.num2.valor()


#ejercicio2

class Alumno:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        #Grupo.anyadir_alumno(self) #No le funcionaba el grupo
        self.asignaturas = []

    def matricular(self, asignatura):
        self.asignaturas.append(asignatura)

    def busca_asig(self, asig):
        for i in self.asignaturas:
            if i == asig:
                return i

            else:

                raise ValueError('NO tienes esa asignatura')


    def set_nota(self, asig, trimestre, nota):
        self.busca_asig(asig).notas[trimestre-1] = nota
        return self


    def media(self, asig):
        suma = 0
        asignatura = self.busca_asig(asig)
        for x in asignatura.notas:
            suma += x
        return suma/asignatura.get_tri()

    def nota(self, asig, tri):
        return self.busca_asig(asig).nota[tri-1]

    def aprobada(self ,asig):
        if self.media(asig) >= 5:
            return True
        else:
            return False


class Grupo:
    def __init__(self) -> None:
        self.grupo = []

    def anyadir_alumno(self, alumno):
        self.grupo.append(alumno)



class Asignatura:
    def __init__(self, denominacio, numtri) -> None:
        self.denom = denominacio
        self.numtri = numtri
        self.notas = []
        for x in range(0, self.numtri):
            self.notas.append(0)

    def get_tri(self):
        return self.numtri

juan = Alumno("Juan")
ingles = Asignatura("ingles", 3)
juan.matricular(ingles)
juan.set_nota(ingles, 1, 1).set_nota(ingles, 2, 3).set_nota(ingles, 3, 6)
