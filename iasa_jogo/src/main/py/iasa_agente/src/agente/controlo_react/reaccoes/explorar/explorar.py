from ecr.comportamento import Comportamento
from random import choice
from sae import Direccao
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

class Explorar(Comportamento):

    """
    Define um comportamento fixo associado à Exploração, com uma resposta fixa, pois gera uma ação em permanência.
    """

    def activar(self, percepcao):

        """
        Ativa o comportamento associado à exploração.
        Na ativação da resposta não é preciso usar o parametro da intensidade
        do método da ativação porque não depende de nenhum estímulo para ser ativado.
        """

        direccao = self.__direccao_aleatoria()
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
    
    def __direccao_aleatoria(self):

        """
        Retorna uma direção aleatória de entre os possíveis valores do enumerado Direccao
        """

        direccoes = list(Direccao)
        return choice(direccoes)