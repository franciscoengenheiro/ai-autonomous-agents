from abc import ABC, abstractmethod


class Avaliador(ABC):

    """
    Representa uma função de avaliação f(n) usada por um algoritmo de procura informada para determinar a ordem de expansão dos nós na fronteira.
    Variantes desta classe podem ser usadas para implementar diferentes algoritmos de procura informada:
    - A* - f(n) = g(n) + h(n)
    - Sofrega - f(n) = h(n)
    - Custo Uniforme - f(n) = g(n)
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Determina a prioridade de um nó na fronteira com base na função de avaliação f(n) que se pode decompor em 2 duas funções distintas:
        - g(n) - o custo do caminho do nó inicial ao nó n.
        - h(n) - o custo estimado do caminho do nó n ao nó objetivo.
        """
    