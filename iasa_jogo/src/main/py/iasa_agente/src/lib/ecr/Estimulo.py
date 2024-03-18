from abc import ABC, abstractmethod

class Estimulo(ABC):
    
    @abstractmethod
    def detectar(self, percepcao):
        """detecta se o estímulo está presente na percepção"""