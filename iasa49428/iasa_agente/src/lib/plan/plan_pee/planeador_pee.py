
from typing import override
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPee
from plan.planeador import Planeador

class PlaneadorPee(Planeador):

    """
    Representa um planeador deliberativo que utiliza um algoritmo de procura de melhor primeiro (e não um em concreto de forma a alterar, possívelmente, o mecanismo de procura dinamicamente), e por isso, especializado em procura em espaço de estados. Responsável por planear a sequência de acções a executar por um agente deliberativo.
    """

    def __init__(self):
        self.__mec_pee: ProcuraMelhorPrim = ProcuraAA()

    @override
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            estado_final = objectivos[0] # porque o mecanismo deliberativo ordena os objetivos por ordem de prioridade (distância ao elemento alvo)
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_pee.procurar(problema, heuristica)
            # Mostrar a solução
            if solucao:
                return PlanoPee(solucao)
        