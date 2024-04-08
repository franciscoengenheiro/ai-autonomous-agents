from agente.controlo_react.reaccoes.aproximar.estímulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

class AproximarDir(Reaccao):
    """
    TODO
    """
    
    def __init__(self, direccao):
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        super().__init__(estimulo, resposta)
