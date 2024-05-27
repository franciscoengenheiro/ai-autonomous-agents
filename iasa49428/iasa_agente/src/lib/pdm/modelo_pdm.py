from abc import ABC, abstractmethod


class ModeloPDM(ABC):

    """
    Define um modelo de um Processo de Decisão de Markov (PDM).
    """
    
    @abstractmethod
    def S(self):

        """
        Representa o conjunto de estados possíveis.
        """
    
    @abstractmethod
    def A(self, s):
        """
        Representa o conjunto de acções possíveis num estado s.
        """

    @abstractmethod
    def T(self, s, a, sn): 
        """
        Representa a probabilidade de transição de um estado s para um estado sn, com base numa acção a.
        """
    
    @abstractmethod
    def R(self, s, a, sn):
        """
        Representa a recompensa de um estado s para um estado sn, com base numa acção a.
        """
    
    @abstractmethod
    def succ(self, s, a):

        """
        Permite obter o estado sucessor de um estado s, com base numa acção a.
        Utiliza a função T para obter o estado sucessor.
        """


    