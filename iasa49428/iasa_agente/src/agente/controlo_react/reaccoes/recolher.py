from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from ecr.hierarquia import Hierarquia
from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.explorar.explorar import Explorar

class Recolher(Hierarquia):

    """
    Representa um comportamento composto com um mecanismo de seleção de ação por hierarquia fixa de prioridade, que corresponde ao objetivo do Agente Prospector de "recolher alvos".
    Associado a este objetivo podem existir os seguintes sub-objetivos:
    - "evitar obstáculos"
    - "aproximar alvo"
    - "explorar"
    """

    def __init__(self):

        """
        Inicializa este comportamento composto com os comportamentos que o compõem pela ordem de prioridade por hierarquia predefinida.
        """
        aproximar_alvo = AproximarAlvo()
        evitar_obst = EvitarObst()
        explorar = Explorar()
        # contar_passos = ContarPassos()
        comportamentos = [aproximar_alvo, evitar_obst, explorar]
        super().__init__(comportamentos)
