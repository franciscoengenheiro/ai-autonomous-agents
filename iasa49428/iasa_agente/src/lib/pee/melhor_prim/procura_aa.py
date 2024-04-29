from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):

    """
    Mecanismo de procura informada baseado no algoritmo de procura A*, caracterizado por uma função de avaliação f(n) = g(n) + h(n). Esta procura é garantidamente ótima, mas é mais lenta que a procura sôfrega mas é garantidamente ótima. Precisa de uma heurística admissível para ser ótima.
    """
    
    def __init__(self):
        avaliador = AvaliadorAA()
        super().__init__(avaliador)
