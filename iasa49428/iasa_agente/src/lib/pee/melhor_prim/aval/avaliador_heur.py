from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorHeur(Avaliador):

    """
    Avaliador baseado numa heurística. Não é usado um construtor, pois a heurística é definida posteriormente (de forma dinâmica).
    """

    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica
    