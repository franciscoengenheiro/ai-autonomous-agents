from typing import override
from plan.plano import Plano

class PlanoPee(Plano):

    """
    Representa um plano de acções a executar por um agente deliberativo, especificamente para a exploração em espaço de estados.
    """
    
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao] # porque a solução é um iterável
    
    @override
    def obter_accao(self, estado):
        if self.__passos:
            primeiro_passo = self.__passos.pop(0)
            if primeiro_passo.estado == estado:
                return primeiro_passo.operador
    
    @override
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)