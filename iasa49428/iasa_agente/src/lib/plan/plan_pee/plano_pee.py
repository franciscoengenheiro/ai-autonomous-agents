from typing import override
from plan.plano import Plano

class PlanoPee(Plano):

    """
    TODO
    """

    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao] # porque a solução é um iterável
    
    @override
    def obter_accao(self, estado):
        """
        Quero a acção para este estado onde o agente se encontra, pois pode ter sido alterado.
        Perceber se é compatível com o plano, e se for, devolve a próxima acção a executar consoante a solução recebida.
        Executar um passo do plano e se esse passo for consistente com o plano atual, então devolve o operador associado a esse passo.
        """
        if self.__passos:
            primeiro_passo = self.__passos.pop(0)
            if primeiro_passo.estado == estado:
                return primeiro_passo.operador
    
    @override
    def mostrar(self, vista):
        """
        TODO
        """

        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)