from plan.plano import Plano


class PlanoPDM(Plano):

    """
    Representa um plano de acções a executar por um agente deliberativo, especificamente para procuras com processos de decisão de Markov (PDM).
    """

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
        
    def mostrar(self, vista):
        if self.__politica:
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
            # mostrar os vetores de politica
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
