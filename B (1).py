"""
En general:
    · No se usan los mecanismos de encapsulación, \
    principalmente los de visibilidad, por lo que \
    algunos métodos sensibles, como los setters, \
    son accesibles, haciendo a los atributos \
        susceptibles de cambios inesperados.
    ·
"""
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
            # Este "aire" -
            else:
            # - no debería estar.
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
        return self.busca_asig(asig).notas[tri-1]    #a notas le faltaba la "s"

    def aprobada(self ,asig):
        if self.media(asig) >= 5:
            return True
        else:
            return False


class Grupo:
    def __init__(self) -> None:
        # Quizá alumnos hubiese sido un nombre más adecuado.
        self.grupo = [] #self.__alumnos = []

    """
    Deberíamos tener accesores y mutadores que garantizen la encapsulación.
    Ej:
    def __get_alumnos(self):
        return self.__grupo

    def __set_alumno(self, alumno):
        if isinstance(alumno, Alumno):
            self.__alumno.append(alumno)
        else: raise TypeError('Los grupos sólo almacenan alumnos.')
    """

    def anyadir_alumno(self, alumno):
        """
        Debería haber un setter que hiciese esta operación, \
        y supongo, porque no tengo los enunciados, que ese \
        setter debe controlar que sólo pudiese recibir \
        instancias de la clase Alumno.
        """
        self.grupo.append(alumno) # self.__set_alumno(alumno)



class Asignatura:
    """
    Podrías añadir un valor por defecto al número de \
    trimestres. Después de todo casi siempre se espera \
    que sean tres.
    """
    def __init__(self, denominacio, numtri = 3) -> None:
        self.denom = denominacio
        self.numtri = numtri
        self.notas = []
        for x in range(self.numtri):
            self.notas.append(0)

    def get_tri(self):
        return self.numtri

"""
Sería más apropiado que los test estuviesen preparados \
para ser ejecutados si ejecutamos este modulo como \
programa principal. Usando:

if __name == '__main__':

Y luego indentamos las siguientes lineas para que estén \
dentro de esa estructura if.
"""
juan = Alumno("Juan")
ingles = Asignatura("ingles", 3)
juan.matricular(ingles)
juan.set_nota(ingles, 1, 1).set_nota(ingles, 2, 3).set_nota(ingles, 3, 6)

"""
Y si yo creo ahora otro alumno, lo matriculo en inglés, \
y le pongo nota, ¿que va a suceder?
"""
paco = Alumno('Paco')
paco.matricular(ingles)
print(f'Recordemos que {juan.nombre} tiene un {juan.nota(ingles, 1)} en '\
    f'el primer trimestre de {juan.busca_asig(ingles).denom}')
paco.set_nota(ingles, 1, 8).set_nota(ingles, 2, 6).set_nota(ingles, 3, 7)
print(f'Si creo a un nuevo alumno que se llama {paco.nombre}, lo matriculo '\
    f'también en {paco.busca_asig(ingles).denom} y le pongo notas...')
print()
print(f'Observa que le pasa a la nota de {juan.nombre}: {juan.nota(ingles, 1)}')
print()
print('El modelado que realizaste para almacenar las notas de los alumnos '\
    'no está funcionando como debería, \npuesto que al poner nota en '\
    f'{ingles.denom} a {paco.nombre}, estamos machacando la nota del último '\
    f'alumno matriculado antes, \nen este caso es {juan.nombre}.')
