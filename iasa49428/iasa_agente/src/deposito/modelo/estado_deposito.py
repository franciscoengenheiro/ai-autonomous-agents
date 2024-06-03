
from mod.estado import Estado


class EstadoDeposito(Estado):

    """
    Mantem informação do volume de água no depósito.
    """

    def __init__(self, valor):
        self.__valor = valor

    def id_valor(self):
        return hash(self.__valor)

    @property
    def volume(self):
        return self.__valor
