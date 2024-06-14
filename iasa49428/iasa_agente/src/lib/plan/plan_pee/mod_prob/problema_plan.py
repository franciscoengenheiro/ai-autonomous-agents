from typing import override
from mod.problema import Problema


class ProblemaPlan(Problema):

    """
    Tendo em conta que o modelo do mundo, num controlo deliberativo, já detem o estado e os operadores, este problema apenas representa um problema de planeamento, com um estado final a atingir. Este problema é utilizado por um planeador para encontrar um plano de ações a executar, dado um modelo do mundo e objetivos a atingir.
    """

    def __init__(self, modelo_plan, estado_final):
        # obter estado inicial de forma dinamica e a partir daí obter operadores
        estado_inicial = modelo_plan.obter_estado()
        operadores = modelo_plan.obter_operadores()
        self.__estado_final = estado_final
        super().__init__(estado_inicial, operadores)
    
    @override
    def objetivo(self, estado):
        return estado == self.__estado_final
