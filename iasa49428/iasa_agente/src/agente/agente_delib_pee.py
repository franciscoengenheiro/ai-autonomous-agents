from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae import Agente

class AgenteDeliberativoPee(Agente):

    """
    Define um Agente com um controlo deliberativo para a procura em espaço de estados (pee).
    """

    def __init__(self):
        planeador = PlaneadorPee()
        controlo_delib = ControloDelib(planeador)
        super().__init__(controlo_delib)
        