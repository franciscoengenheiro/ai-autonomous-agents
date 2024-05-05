from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Representação uma ação geradora de uma transição de um estado para outro. No âmbito do raciocínio automático, os operadores abstraem as transformações (dinâmicas) que ocorrem. Associado a um operador está uma função que gera o estado sucessor a partir de um estado dado e uma função que define o custo associado à transição de um estado para outro.
    Nota: Não confundir operador com transição. O operador é uma ação que gera uma transição de um estado para outro, enquanto que a transição é a passagem de um estado para outro.
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Gera a transformação de um estado para outro.
        """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Define o custo associado à transição de um estado para outro.
        """
