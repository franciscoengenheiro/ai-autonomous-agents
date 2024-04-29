from pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):

    """
    Representa uma fronteira ao qual está associada uma função de avaliação f(n) que ordena os nós de forma a que o nó com menor valor de avaliação seja o primeiro a ser retirado da fronteira.
    """
    
    def __init__(self, avaliador):
        self._avaliador = avaliador
    
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no)
        # Um tuplo é criado com:
        # - o valor da prioridade
        # - o nó, porque a prioridade é usada para ordenar os nós
        heappush(self._nos, (prioridade, no))

    def remover(self):
        # Não é feita um estado de verificação para ver se a fronteira está vazia porque a função heappop() lança uma exceção IndexError se a fronteira estiver vazia e porque, segundo o algoritmo de procura, a fronteira nunca estará vazia porque termina quando a fronteira está vazia
        # O nó com menor prioridade é retirado da fronteira
        (_, no) = heappop(self._nos)
        return no