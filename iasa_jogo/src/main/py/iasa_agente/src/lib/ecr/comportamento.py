from abc import ABC, abstractmethod
    
class Comportamento:

    """
    Encapsula um conjunto de reações relacionadas entre si, possivelmente com uma sequência temporal, de forma a atingir um objetivo.

    Tipos de Comportamento:
    - Comportamento Simples (Reação)
    - Comportamento Composto (Seleção de Ação)
    """

    @abstractmethod
    def ativar(self, percepcao):
        """
        TODO
        """