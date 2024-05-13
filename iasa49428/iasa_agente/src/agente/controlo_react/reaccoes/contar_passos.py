from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.comportamento import Comportamento
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao

class ContarPassos(Comportamento):
    
    """
    Define um comportamento fixo com memória ou estado que está associado ao objetivo "contar passos". Caracteriza-se por ter uma resposta fixa, pois gera uma ação em permanência, que consiste em mover-se numa direção fixa (Norte) após o Agente ter efetuado 10 passos. Não depende de nenhum estímulo para ser ativado.
    """

    def __init__(self):
        self.__passos = 0
        self.__resposta = RespostaMover(Direccao.NORTE)

    def activar(self, percepcao):

        """
        Se este método não retornar nenhuma ação, então o comportamento seguinte é selecionado da
        da lista de comportamentos do comportamento composto, que utiliza uma hierarquia de comportamentos
        """

        self.__passos += 1
        print(f"Passos: {self.__passos}")

        if self.__passos >= 10:
            return self.__resposta.activar(percepcao)        
