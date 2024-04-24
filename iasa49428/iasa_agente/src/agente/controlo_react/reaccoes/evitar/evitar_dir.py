from agente.controlo_react.reaccoes.evitar.estímulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

class EvitarDir(Reaccao):

    """
    Reacção que faz o agente mover-se numa direção livre de obstáculos
    """

    def __init__(self, direccao, resposta):
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, resposta)
