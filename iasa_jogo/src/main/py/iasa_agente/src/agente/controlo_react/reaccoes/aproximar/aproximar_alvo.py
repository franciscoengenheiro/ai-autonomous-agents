from ecr.prioridade import Prioridade
from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from sae import Direccao

class AproximarAlvo(Prioridade):

    """
    Representa um comportamento composto com um mecanismo de seleção de ação por prioridade, que corresponde ao objetivo do Agente Prospector de se "aproximar de um alvo".
    """

    def __init__(self):

        aproximar_dir_este = AproximarDir(Direccao.ESTE)
        aproximar_dir_oeste = AproximarDir(Direccao.OESTE)
        aproximar_dir_norte = AproximarDir(Direccao.NORTE)
        aproximar_dir_sul = AproximarDir(Direccao.SUL)
        comportamentos = [aproximar_dir_este, aproximar_dir_oeste, aproximar_dir_norte, aproximar_dir_sul]
        super().__init__(comportamentos)