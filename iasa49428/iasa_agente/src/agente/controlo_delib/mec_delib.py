from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae.ambiente.elemento import Elemento

class MecDelib:

    """
    Representa um mecanismo deliberativo. Inerente a um processo em que o agente intencionalmente, com o proposito de atingir um determinado objetivo, simula as situações futuras (antecipação), avalia as consequências das suas ações e escolhe a melhor ação a executar (deliberação).
    """

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
    
    def deliberar(self):
        
        """
        Gera uma lista de objetivos, estados. Neste caso, a lista de objetivos é composta por posições que contêm o elemento alvo. Como cada objetivo é um estado, é feita uma ordenação dos objetivos com base na distância euclidiana entre a posição atual do agente e a posição do objetivo.
        """
        
        estados = self.__modelo_mundo.obter_estados()
        objetivos = list(filter(lambda elem: self.__modelo_mundo.obter_elemento(elem) == Elemento.ALVO, estados))
        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia) # função de avaliação
            return objetivos
