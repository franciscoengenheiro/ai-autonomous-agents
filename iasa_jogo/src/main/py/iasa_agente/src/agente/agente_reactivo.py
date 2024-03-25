from sae import Agente
from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar

class AgenteReactivo(Agente):

    """
    Define um agento reativo com
    """

    def __init__(self):
        comportamento = Explorar()
        controlo_reativo = ControloReact(comportamento)
        super().__init__(controlo_reativo)
        