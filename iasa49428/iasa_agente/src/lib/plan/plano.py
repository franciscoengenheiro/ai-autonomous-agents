from abc import ABC, abstractmethod

class Plano(ABC):
    
    @abstractmethod
    def obter_accao(self, estado):
        """
        TODO
        """

    @abstractmethod
    def mostrar(self, vista):
        """
        TODO
        """
    