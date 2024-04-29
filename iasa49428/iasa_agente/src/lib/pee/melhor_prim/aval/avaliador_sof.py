from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):

    """
    Define um avaliador baseado no algoritmo de procura informada sofrega,caracterizado por uma função de avaliação f(n) = h(n).
    """

    def prioridade(self, no):
        return self._heuristica.h(no.estado)