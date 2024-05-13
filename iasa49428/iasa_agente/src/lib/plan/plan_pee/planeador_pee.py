
from typing import override
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPee
from plan.planeador import Planeador

class PlaneadorPee(Planeador):

    """
    TODO
    """

    def __init__(self):
        self.__mec_pee: ProcuraMelhorPrim = ProcuraAA()

    @override
    def planear(self, modelo_plan, objectivos):
        """
        TODO
        """
    
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_pee.procurar(problema, heuristica)

            # Mostrar a solução
            if solucao:
                return PlanoPee(solucao)
        