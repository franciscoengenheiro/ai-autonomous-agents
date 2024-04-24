from ecr.comportamento import Comportamento
from random import choice
from sae import Direccao
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

class Explorar(Comportamento):

    """
    Define um comportamento fixo sem memória (i.e., representação interna de percepções anteriores) e que, por isso está condenado à repetição. Está associado ao objetivo "explorar" e caracteriza-se por ter uma resposta fixa, pois gera uma ação em permanência, que consiste em mover-se numa direção aleatória. Não depende de nenhum estímulo para ser ativado.
    """

    def activar(self, percepcao):

        """
        Ativa a funcionalidade que este comportamento representa consoante a perceção recebida.
        Na ativação da resposta não é preciso usar o paramêtro intensidade do método da ativação porque não depende de nenhum estímulo para ser ativado, relembrando que uma resposta pode ser ativada tanto por um estímulo como por uma percepção diretamente.
        """

        direccao = self.__direccao_aleatoria()
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)

    def __direccao_aleatoria(self):

        """
        Retorna uma direção aleatória de entre os possíveis valores no plano cartesiano.
        """

        direccoes = list(Direccao)
        return choice(direccoes)
