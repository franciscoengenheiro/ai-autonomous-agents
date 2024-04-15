from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Fronteira de exploração que representa os nós folhas da árvore de procura. Estes nós são candidatos a serem expandidos. A forma como é feita essa escolha dependerá da estratégia de procura utilizada.
    """

    @property
    def vazia(self):
        """
        Propriedade derivada. 
        Indica se a fronteira está vazia.
        """
        return self.dimensao() == 0
    
    @property
    def dimensao(self):
        """
        Propriedade derivada é uma propriedade onde o seu valor é calculado em tempo de execução. 
        Indica a dimensão da fronteira, ou seja, o número de nós que a compõem.
        """
        return len(self._nos)

    def __init__(self):
        # Exemplo de fatorização comportamental
        self.iniciar()

    def iniciar(self):

        """
        Inicializa a estrutura de dados que representa os elementos iniciais da fronteira.
        """
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        """
        Insere um nó na fronteira.
        """
    
    def remover(self):
        """
        Remove um nó da fronteira se a fronteira não estiver vazia e devolve-o.
        """        
        if self.vazia:
            return self._nos.pop(0)
