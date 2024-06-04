from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente

class AgenteDeliberativoPDM(Agente):

    """
    Define um Agente com um controlo deliberativo para a procura com processos de decisão de Markov (pdm).
    """

    def __init__(self):
        planeador = PlaneadorPDM(gama=0.98) # o gama aumenta o nr de iterações para a convergência disparar
        controlo_delib = ControloDelib(planeador)
        super().__init__(controlo_delib)
