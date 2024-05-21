from abc import ABC, abstractmethod



class ModeloPDM(ABC):

    """
    TODO
    """
    
    @abstractmethod
    def S(self):

        """
        TODO
        """

        raise NotImplementedError("Not implemented yet")
    
    @abstractmethod
    def A(self, s):

        """
        TODO
        """

        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def T(self, s, a, sn):
            
        """
        TODO
        """

        raise NotImplementedError("Not implemented yet")
    
    @abstractmethod
    def R(self, s, a, sn):
        raise NotImplementedError("Not implemented yet")
    
    @abstractmethod
    def succ(self, s, a):

        """
        Permite obter o estado sucessor de um estado s, com base numa acção a.
        Utiliza a função T para obter o estado sucessor.
        """

        raise NotImplementedError("Not implemented yet")


    