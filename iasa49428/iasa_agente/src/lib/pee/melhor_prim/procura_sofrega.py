from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):

    """
    Mecanismo de procura informada, de melhor primeiro, onde a função de avaliação é a distância ao objetivo (f(n) = h(n)). É exponentialmente mais eficiente que a procura de custo uniforme, porque é seletiva, no entanto não é garantidamente ótima. Variante da procura melhor primeiro, tipo de procura informada.
    """

    def __init__(self):
        avaliador = AvaliadorSof()
        super().__init__(avaliador)
