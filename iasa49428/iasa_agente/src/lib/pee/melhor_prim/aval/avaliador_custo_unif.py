from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):

    """
    Define um avaliador baseado no algoritmo de procura não informada de custo uniforme, caracterizada por uma função de avaliação f(n) = g(n).
    """

    def prioridade(self, no):
        return no.custo
    