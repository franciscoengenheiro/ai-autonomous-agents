from pee.melhor_prim.aval.heuristica import Heuristica


class HeuristicaContagem(Heuristica):
    # que reflita distancia entre valores, para o sistema poder optar por transições de estado que minimizam a distância ao estado objetivo

    """
    Define a heurística baseada na contagem de valores. No contexto do dominio do problema de contagem, esta heurística é admissível pois representa a distância minima entre o valor do estado atual e o valor do estado final.
    """

    def __init__(self, valor_final):
        self.valor_final = valor_final

    def h(self, estado):
        # a distância entre os valores dos estados
        return abs(estado.valor - self.valor_final)
