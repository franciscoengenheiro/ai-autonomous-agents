from abc import ABC, abstractmethod

class Heuristica(ABC):

    """
    Representa uma heurística que pode ser utilizada por um algoritmo de procura informada para estimar o custo de um estado atingir o estado objetivo, é possível que não seja admissível, ou seja, que não seja menor ou igual ao custo real.
    """
    
    @abstractmethod
    def h(self, estado):
        """
        Representa uma função que calcula a estimativa do custo h(n) de um nó a partir do estado (n) atingir o estado objetivo. sem que o percurso tenha sido previamente explorado.
        """