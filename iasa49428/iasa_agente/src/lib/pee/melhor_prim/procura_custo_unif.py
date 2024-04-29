from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):

    """
    Baseada na procura grafo com a diferença que a fronteira é ordenada de acordo com a função de avaliação, a procura é feita pelo nó com menor valor de avaliação, neste caso o seu custo.
    """

    def __init__(self):
        avaliador = AvaliadorCustoUnif()
        super().__init__(avaliador)
        