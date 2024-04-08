from sae import Agente
from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
# from agente.controlo_react.reaccoes.recolher import Recolher   

class AgenteReactivo(Agente):

    """
    Define um Agente com um controlo reativo ao qual está associado um comportamento, sendo que este pode ser composto por sub-comportamentos.
    """

    def __init__(self):
        comportamento = Explorar()
        # comportamento = Recolher()
        controlo_reativo = ControloReact(comportamento)
        controlo_reativo.mostrar_per_dir = True
        super().__init__(controlo_reativo)
        