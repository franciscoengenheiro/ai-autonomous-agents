from mod.estado import Estado

class EstadoAgente(Estado):

    """
    Representação de um estado do agente. Um estado é caracterizado pela sua posição no ambiente.
    """
    
    def __init__(self, posicao):
        self.__posicao = posicao

    @property
    def posicao(self):
        return self.__posicao
    
    def id_valor(self):
        return hash(self.__posicao)