from mod_prob.estado_contagem import EstadoContagem
from mod_prob.operador_incremento import OperadorIncremento
from mod.problema import Problema


class ProblemaContagem(Problema):

    """
    Define um problema de contagem:
    - Dado um valor inicial, um valor final e um conjunto de incrementos possíveis, que incrementos realizar para atingir ou superar o valor final.
    - Exemplo: Se o valor inicial for 0, o valor final for 9 e os incrementos possíveis forem [1, 2], então a solução deverá ser: 0, 2, 4, 6, 8, 9, com os incrementos 2, 2, 2, 2, 1.
    """

    def __init__(self, valor_inicial, valor_final, incrementos):
        self.__valor_final = valor_final
        operadores = [OperadorIncremento(incremento) for incremento in incrementos]
        super().__init__(EstadoContagem(valor_inicial), operadores)

    def objetivo(self, estado):
        """
        O objetivo final é atingir ou superar o valor final.
        """

        return estado.valor >= self.__valor_final