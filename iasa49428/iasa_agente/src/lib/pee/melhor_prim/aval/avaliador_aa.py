from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):

    """
    Define um avaliador baseado no algoritmo de procura informada A*, caracterizado pela existência de uma heurística admissível e por uma função de avaliação f(n) = g(n) + h(n).
    """

    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)