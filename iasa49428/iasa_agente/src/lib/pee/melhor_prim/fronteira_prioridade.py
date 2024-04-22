from pee.mec_proc.fronteira import Fronteira


class FronteiraPrioridade(Fronteira):

    """
    Representa uma fronteira ao qual está associada uma função de avaliação que ordena os nós de forma a que o nó com menor valor de avaliação seja o primeiro a ser retirado da fronteira.
    """
    
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador
    
    def inserir (self, no):
        raise NotImplementedError()

    def remover(self):
        raise NotImplementedError()