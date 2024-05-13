from abc import ABC, abstractmethod

class Plano(ABC):

    """
    Representa um plano de ações a executar por um agente deliberativo. 
    Associado a um plano está um planeador que o produz, com base num modelo do mundo e num conjunto de objetivos a atingir.
    O plano pode ser alterado consoante o tempo, por exemplo, se o agente se desviar do plano original e é a responsabilidade deste módulo detetar essa situação e informar o planeador.
    """
    
    @abstractmethod
    def obter_accao(self, estado):
        """
        Devolve a próxima acção a ser executada, representada através do seu operador.
        """

    @abstractmethod
    def mostrar(self, vista):
        """
        Mostra o plano na vista associada a um controlo de agente
        """
    