from ecr.comportamento import Comportamento
from abc import abstractmethod

class ComportComp(Comportamento): 

    """
    Mecanismo de reação que agrega conjuntos de comportamentos. Está inerente a um comportamento composto, o problema de seleção de acção que é resolvido através da seleção de uma acção apropriada, a partir de um conjunto de acções possíveis, em função das percepções do agente.
    """

    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
    
    def activar(self, percepcao):
        """
        A ativação de um comportamento composto consiste em iterar cada comportamento que o compõe e ativá-lo com a percepção recebida.
        No final é utilizado o mecanismo de seleção de acção para determinar a acção a realizar em função das acçoes obtidas pela ativação dos comportamentos.
        """
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)

        if accoes:
            return self.seleccionar_accao(accoes)
            
    @abstractmethod
    def seleccionar_accao(accoes):
        """
        Define o módulo de seleção de ação associado a um comportamento composto.
        Mecanismos de combinação e seleção de acções:
        - Execução paralela de ações (As ações são executadas em paralelo porque não interferem entre si);
        - Seleção por prioridade (As ações são selecionadas em função de uma prioridade);
        - Combinação de ações (As ações são combinadas numa única resposta por composição e.g., soma vectorial);
        - Seleção aleatória (As ações são selecionadas aleatoriamente)
        """
    