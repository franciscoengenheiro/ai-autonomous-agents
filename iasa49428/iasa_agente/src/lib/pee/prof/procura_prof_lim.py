from pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    """
    Representa um mecanismo de procura em profundidade limitada com uma fronteira LIFO. A diferença para a pesquisa em profundidade é que a pesquisa é limitada a uma profundidade máxima. Quando essa profundidade é atingida, a pesquisa continua para o nó seguinte na fronteira.
    """

    def __init__(self, prof_max=500):
        super().__init__()
        self.__prof_max = prof_max

    @property
    def prof_max(self):
        return self.__prof_max

    @prof_max.setter
    def prof_max(self, valor):
        self.__prof_max = valor

    def _expandir(self, problema, no):
        """
        O nó só é expandido se a profundidade do nó for inferior à profundidade máxima. De forma a que a lista retornada por este método continue a ser iterada, é retornado uma lista vazia e não None.
        """
        list = []
        if no.profundidade < self.__prof_max:
            list = super()._expandir(problema, no)
        return list
