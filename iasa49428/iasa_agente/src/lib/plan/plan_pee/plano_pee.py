from typing import override
from plan.plano import Plano

class PlanoPee(Plano):

    """
    TODO
    """

    def __init__(self, solucao):
        raise NotImplementedError
    
    @override
    def obter_accao(self, estado):
        """
        TODO
        """
        raise NotImplementedError
    
    def valido(self, estado):
        """
        TODO
        """
        raise NotImplementedError
    
    @override
    def mostrar(self, vista):
        """
        TODO
        """
        raise NotImplementedError