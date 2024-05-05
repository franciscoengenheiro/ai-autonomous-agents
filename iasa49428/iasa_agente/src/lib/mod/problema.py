from abc import ABC, abstractmethod

class Problema(ABC):

    """
    Dá suporte ao raciocínio automático representado modelando um problema com um estado objetivo. Associado a um problema estão um estado inicial e um conjunto de operadores que permitem a transição entre estados, bem como uma função predicado que verifica se um estado é um estado objetivo.
    """

    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
        """
        Função predicado que verifica se o estado passado como argumento é um estado objetivo. Permitindo, desta forma, a resolução do problema associado.
        """

    @property # equivalente a um getter do Java
    def estado_inicial(self):

        """
        Retorna o estado inicial usado para instanciar este problema.
        """

        return self.__estado_inicial

    @property
    def operadores(self):

        """
        Retorna os operadores usados para instanciar este problema.
        """

        return self.__operadores
