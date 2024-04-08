from ecr.estimulo import Estimulo
from sae import Elemento

"""
Representa um estímulo que deteta a presença de um elemento numa determinada direção.
"""
class EstimuloAlvo(Estimulo):

    def __init__(self, direccao, gama : float = 0.9):
        self.__gama = gama
        self.__direccao = direccao

    """
    Consiste em detetar a presença de um alvo numa determinada direção, com base na percepção recebida.
    A prioridade da resposta é inversamente proporcional à distância, ou seja, quanto menor a distância maior a intensidade
    """
    def detectar(self, percepcao):
        elemento, distancia, posicao = percepcao[self.__direccao]
        intensidade = 0.0
        if elemento == Elemento.ALVO:
            # função exponencial com base no gama e na distância
            intensidade = self.__gama**distancia 
        return intensidade

        
        
    