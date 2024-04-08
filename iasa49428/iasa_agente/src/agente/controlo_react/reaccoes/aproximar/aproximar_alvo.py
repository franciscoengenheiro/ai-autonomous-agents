from ecr.prioridade import Prioridade
from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):

    """
    Representa um comportamento composto com um mecanismo de seleção de ação por prioridade, que corresponde ao objetivo do Agente prospector de se: "aproximar de um alvo".
    """

    def __init__(self):
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]
        super().__init__(comportamentos)
