from abc import ABC, abstractmethod

class Estimulo(ABC):

    """
    Define a informação que é extraída de uma percepção, de forma a ser utilizada na ativação de comportamentos. Vários estimulos podem ser ativados por uma única percepção.
    """
    
    @abstractmethod
    def detectar(self, percepcao):
        """
        A deteção de um estimulo consiste em extraír informação relevante de uma percepção
        TODO: falar sobre o retorno depois de implementar
        """
    