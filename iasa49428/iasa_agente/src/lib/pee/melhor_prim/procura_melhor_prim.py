from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGrafo):
    """
    Baseada na procura por grafo com a diferença que a fronteira é ordenada de acordo com a função de avaliação, a procura é feita pelo nó com menor valor de avaliação. A função de avaliação é passada como argumento ao construtor, e que avalia a prioridade de um nó (e.g., distância ao objetivo, tempo, custo). Ordenação da fronteira ocorre quando é inserido um valor.
    """

    def __init__(self, avaliador):
        self._avaliador = avaliador
        frontPrioridade = FronteiraPrioridade(avaliador)
        super().__init__(frontPrioridade)
    
    def _manter(self, no):
        """
        Em relação à funcionalidade da procura em grafo, de forma a que o nó possa ser mantido, além de não estar nos nós explorados, o custo do nó tem de ser menor que o custo do nó explorado.
        """

        return super()._manter(no) or no.custo < self._explorados[no.estado].custo
    