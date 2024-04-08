from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):
    
    """
    Representa um comportamento composto com um mecanismo de seleção de ação por hierarquia fixa de prioridade, que corresponde ao objetivo do Agente prospector de "evitar obstáculos".
    """

    def __init__(self):
        self.__resposta_evitar = RespostaEvitar()
        comportamentos = [EvitarDir(direccao, self.__resposta_evitar) for direccao in Direccao]
        super().__init__(comportamentos)
