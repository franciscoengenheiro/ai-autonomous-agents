from math import dist
from typing import override
from pee.melhor_prim.aval.heuristica import Heuristica


class HeurDist(Heuristica):

    """
    Heurística que calcula a distância euclidiana entre duas posições no plano.
    """

    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    @override
    def h(self, estado):
        return dist(self.__estado_final.posicao, estado.posicao)