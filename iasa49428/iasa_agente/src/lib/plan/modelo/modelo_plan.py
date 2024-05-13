from abc import ABC, abstractmethod

class ModeloPlan(ABC):

    @abstractmethod
    def __obter_estado(self):
        """
        TODO RETORNA UM PLANO
        """

    @abstractmethod
    def __obter_estados(self):
        """
        TODO
        """

    @abstractmethod
    def __obter_operadores(self):
        """
        TODO
        """
    