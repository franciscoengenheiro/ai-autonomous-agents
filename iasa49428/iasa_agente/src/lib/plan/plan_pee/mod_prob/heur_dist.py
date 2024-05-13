from typing import override
from pee.melhor_prim.aval.heuristica import Heuristica


class HeurDist(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final
        raise NotImplementedError
    
    @override
    def h(self, estado):
        raise NotImplementedError