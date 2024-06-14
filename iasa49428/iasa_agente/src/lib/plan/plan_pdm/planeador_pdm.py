from pdm.pdm import PDM
from plan.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador


class PlaneadorPDM(Planeador):

    """
    Representa um planeador deliberativo que utiliza um processo de decisão de Markov (PDM) para encontrar um plano de ações consoante os objetivos a atingir.
    """

    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):

        if objectivos:
            # instancia o modelo pdm (modelopdmplan)
            modelo_plan = ModeloPDMPlan(modelo_plan, objectivos)
            pdm = PDM(modelo_plan, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()
            return PlanoPDM(utilidade, politica)
