from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):

    """
    Representa um mecanismo de procura em profundidade com uma fronteira LIFO. Caracteriza-se por explorar um ramo de pesquisa até ao fim antes de explorar outro ramo - pesquisa em profundidade. Caracteriza-se por não garantir uma solução completa e muito menos ótima.
    - Complexidade temporal: O(b^m) (exponencial)
    - Complexidade espacial: O(bm) (linear)
    Onde b é o fator de ramificação e m é a profundidade máxima da árvore de pesquisa.
    """
    
    def __init__(self):
        super().__init__(FronteiraLIFO())
    
    def _memorizar(self, no):
        self._fronteira.inserir(no)
        