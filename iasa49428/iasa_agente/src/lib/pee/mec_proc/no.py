class No:

    """
    Representa um nó de uma árvore de procura.
    É composto por um:
    - estado: estado que o nó representa
    - operador: operador que foi aplicado para gerar a transição do estado do nó para o estado sucessor
    - antecessor: nó antecessor ao qual foi aplicado o operador para gerar este nó
    - profundidade: profundidade do nó na árvore de procura (i.e., incremental a cada nível da árvore de procura)
    - custo: custo associado ao caminho que vai do nó raiz ao nó (i.e., incremental a cada transição de um nó para o nó sucessor)
    """

    def __init__(self, estado, operador = None, antecessor = None, custo = 0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__profundidade = 0
        if self.__antecessor is not None:
            self.__profundidade = self.__antecessor.profundidade + 1
        self.__custo = custo

    def __lt__(self, no): # makes a comparable class with the less than operator
        return self.custo < no.custo

    @property
    def custo(self):
        return self.__custo

    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor