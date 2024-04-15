from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Representação uma ação geradora de uma transição de um estado para outro. No âmbito do raciocínio automático, os operadores abstraem as transformações (dinâmicas) que ocorrem.
    """
    
    @abstractmethod
    def aplicar(self, estado):
        """
        Gera o estado sucessor a partir do estado passado como argumento.
        """
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Define o custo associado à transição de um estado para outro.
        """