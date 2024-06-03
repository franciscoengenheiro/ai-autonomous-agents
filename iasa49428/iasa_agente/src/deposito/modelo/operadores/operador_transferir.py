from abc import abstractmethod
from math import cos, dist
from math import sin
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador


class OperadorTransferir(Operador):

    def __init__(self, volume):
        self._volume = volume

    @abstractmethod
    def aplicar(self, estado):
        """
        TODO
        """

    def custo(self, estado, estado_suc):
        """
        TODO
        """

        return abs(estado.volume - estado_suc.volume) ** 2
