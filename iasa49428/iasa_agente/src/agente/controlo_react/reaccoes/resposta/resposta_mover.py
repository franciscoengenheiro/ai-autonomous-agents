from ecr.resposta import Resposta
from sae import Accao

class RespostaMover(Resposta):

    """
    Representa uma resposta de um agente para se mover numa direção alvo.
    """
    def __init__(self, direcao):
        accao = Accao(direcao)
        super().__init__(accao)