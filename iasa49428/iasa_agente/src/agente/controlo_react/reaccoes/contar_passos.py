from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.comportamento import Comportamento
# from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao

class ContarPassos(Comportamento):

    """
    TODO
    """

    def __init__(self):
        self.__passos = 0
        aproximar_dir_norte = AproximarDir(Direccao.NORTE)
        self.__resposta = RespostaMover(aproximar_dir_norte)

    def activar(self, percepcao):

        """
        each time this method is called means that the agent is taking action
        for each step the agent takes, it will increment the number of steps taken
        and shows the number of steps taken in the console
        when 10 steps are taken, the agent will move North
        """ 

        self.__passos += 1
        print(f"Passos: {self.__passos}")

        """
        If no action is returned by this method then the next behaviour is selected from
        the list of behaviours in the Recolher class which uses a hierarchy of behaviours
        """
        if self.__passos >= 10:
            return self.__resposta.activar(percepcao)        
