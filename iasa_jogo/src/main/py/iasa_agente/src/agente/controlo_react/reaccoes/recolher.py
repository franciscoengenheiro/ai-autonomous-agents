from ecr.hierarquia import Hierarquia
from agente.controlo_react.reaccoes.aproximar import AproximarAlvo
from agente.controlo_react.reaccoes.evitar import EvitarObst
from agente.controlo_react.reaccoes.explorar import Explorar

class Recolher(Hierarquia):

    """
    Representa um comportamento composto com um mecanismo de seleção de ação por hierarquia fixa de prioridade, que corresponde ao objetivo do Agente Prospector de "recolher alvos". 
    Associado a este objetivo podem existir os seguintes sub-objetivos:
    - "evitar obstáculos" 
    - "aproximar alvo"
    - "explorar"
    """

    def __init__(self, comportamentos):

        """
        Inicializa este comportamento composto com os comportamentos que o compõem pela ordem de prioridade por hierarquia predefinida.
        """
        aproximar_alvo = AproximarAlvo()
        evitar_obst = EvitarObst()
        explorar = Explorar()
        # comportamentos = [aproximar_alvo, evitar_obst, explorar]
        comportamentos = [explorar]
        super().__init__(comportamentos)


    