from mod_prob.estado_contagem import EstadoContagem
from mod.operador import Operador


class OperadorIncremento(Operador):

    """
    Define um operador de incremento, que incrementa o valor de um estado com um determinado valor.
    Exemplo: Se o incremento for 2, então o valor do estado sucessor será o valor do estado atual mais 2.
    """

    def __init__(self, incremento):
        self.__incremento = incremento

    @property
    def incremento(self):
        return self.__incremento

    def aplicar(self, estado):

        """
        Neste contexto, este método é responsável por gerar o estado sucessor a partir do estado passado como argumento. O estado sucessor é obtido através da adição do incremento ao valor do estado passado como argumento.
        """

        return EstadoContagem(estado.valor + self.__incremento)
    
    def custo(self, estado, estado_suc):

        """
        Sabendo que o custo associado à transição de um estado para outro é igual ao quadrado do incremento, este método é responsável por calcular o custo associado à transição de um estado para outro. Neste caso, o custo não depende do estado sucessor nem do estado atual.
        """

        return self.__incremento ** 2