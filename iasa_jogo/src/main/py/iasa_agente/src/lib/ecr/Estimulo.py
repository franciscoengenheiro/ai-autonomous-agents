from abc import ABC, abstractmethod

class Estimulo(ABC):

    """
    Define a informação inerente a uma determinada reacção.
    TODO
    """
    
    @abstractmethod
    def detectar(self, percepcao):
        """
        """