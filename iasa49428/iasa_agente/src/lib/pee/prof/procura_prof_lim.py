from pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):

    """
    Representa um mecanismo de procura em profundidade limitada com uma fronteira LIFO. A diferença para a pesquisa em profundidade é que a pesquisa é limitada a uma profundidade máxima. Quando essa profundidade é atingida, a pesquisa continua para o nó seguinte na fronteira.
    """

    def __init__(self, prof_max = 500):
        super().__init__()
        self.__prox_max = prof_max

    @property
    def prox_max(self):
        return self.__prox_max
    
    @prox_max.setter
    def prox_max(self, valor):
        self.__prox_max = valor

    def _expandir(self, problema, no):

        """
        O nó só é expandido se a profundidade do nó for inferior à profundidade máxima. De forma a que a lista retornada por este método continue a ser iterada, é retornado uma lista vazia e não None.
        """
        list = []
        if no.profundidade < self.__prox_max:
            list = super()._expandir(problema, no)
        return list