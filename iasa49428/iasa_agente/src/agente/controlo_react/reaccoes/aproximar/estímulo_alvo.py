from ecr.estimulo import Estimulo
from sae import Elemento

class EstimuloAlvo(Estimulo):

    """
    Representa um estímulo que deteta a presença de um elemento numa determinada direção e ao qual está associada uma intensidade.
    """

    def __init__(self, direccao, gama : float = 0.9):
        self.__gama = gama
        self.__direccao = direccao

    """
    Consiste em detetar a presença de um alvo numa determinada direção, com base na percepção recebida.
    A prioridade desta resposta vai ser inversamente proporcional à distância, ou seja, quanto menor a distância maior a intensidade (i.e., comportamento obtido através da função exponencial com base no gama e na distância).
    """
    def detectar(self, percepcao):
        elemento, distancia, posicao = percepcao[self.__direccao]
        intensidade = 0.0 # edit: 0 (int) -> 0.0 (float)
        if elemento == Elemento.ALVO:
            intensidade = self.__gama**distancia
        return intensidade



