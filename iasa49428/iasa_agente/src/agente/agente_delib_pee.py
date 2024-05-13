from agente.controlo_delib.controlo_delib import ControloDeliberativo
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae import Agente

class AgenteDeiberativoPee(Agente):

    """
    Define um Agente com um controlo deliberativo para a procura em espaço de estados (pee).
    """

    def __init__(self):
        planeador = PlaneadorPee()
        controlo_delib = ControloDeliberativo(planeador)
        super().__init__(controlo_delib)
        