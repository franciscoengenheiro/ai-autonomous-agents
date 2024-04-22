from mod.estado import Estado


class EstadoContagem(Estado):

    """
    Representa um estado de um problema de contagem. Caracteriza-se por possuir um valor numérico associado (e.g, 0, 1, 2, 3, ...).
    """

    def __init__(self, valor):
        self.__valor = valor

    def id_valor(self):
        return hash(self.__valor)

    @property
    def valor(self):
        return self.__valor