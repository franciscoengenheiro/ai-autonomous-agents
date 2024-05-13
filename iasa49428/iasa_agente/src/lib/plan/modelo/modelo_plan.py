from abc import ABC, abstractmethod

class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """
        Retorna o estado atual do agente.
        """

    @abstractmethod
    def obter_estados(self):
        """
        Retorna os estados das posições válidas.
        """

    @abstractmethod
    def obter_operadores(self):
        """
        Retorna os operadores utilizados para gerar os estados sucessores, associados a este modelo.
        """
    