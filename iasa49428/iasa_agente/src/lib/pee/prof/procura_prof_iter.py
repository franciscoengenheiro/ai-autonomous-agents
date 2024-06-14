from typing import override
from pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """
    Representa um mecanismo de procurar em profundidade iterativa, baseada na procura em profundidade limitada. A procura é feita com incrementos de profundidade, até um limite máximo de profundidade.
    """

    def __init__(self):
        self.__nos_processados = 0
        super().__init__()

    def procurar(self, problema, inc_prof=1, lim_prof=1000):
        """
        Procura a solução para o problema, com incrementos de profundidade até um limite máximo de profundidade. Termina quando encontra uma solução ou atinge o limite máximo de profundidade. Se incremento de profundidade for maior que 1, deixa de ser uma procura ótima.
        """

        # lim_prof + 1 porque a função range não inclui o último valor (exclusivo)
        for profundidade in range(0, lim_prof + 1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            self.__nos_processados += super().get_nos_processados()
            if solucao:
                return solucao

    @override
    def get_nos_processados(self):
        return self.__nos_processados
