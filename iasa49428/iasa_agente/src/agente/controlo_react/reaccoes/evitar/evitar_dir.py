from agente.controlo_react.reaccoes.evitar.estímulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

class EvitarDir(Reaccao):
    
    """
    Reacção que faz o agente mover-se na direcção oposta ao obstáculo.
    """
    
    def __init__(self, direccao, resposta):
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, resposta)
        