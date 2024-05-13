from abc import ABC, abstractmethod

class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """
        TODO RETORNA UM PLANO
        """

    @abstractmethod
    def obter_estados(self):
        """
        TODO
        """

    @abstractmethod
    def obter_operadores(self):
        """
        TODO
        """
    