from ecr.resposta import Resposta
from sae import Accao

class RespostaMover(Resposta):

    """
    Representa um ação de movimento numa direção indicada no construtor.
    """
    def __init__(self, direcao):
        # TODO: is direccao needed as self.direccao?
        accao = Accao(direcao)
        super().__init__(accao)