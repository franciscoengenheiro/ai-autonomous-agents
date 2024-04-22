from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    """
    Representa um mecanismo de procura em grafo com uma fronteira FIFO. Caracteriza-se por explorar todos os nós de um nível antes de passar para o nível seguinte - pesquisa em largura. Caracteriza-se por garantir uma solução completa e ótima.
    - Complexidade temporal: O(b^d) (exponencial) 
    - Complexidade espacial: O(b^d) (exponencial)
    Onde b é o fator de ramificação e d é a profundidade da solução.
    """
    
    def __init__(self):
        super().__init__(FronteiraFIFO())
        