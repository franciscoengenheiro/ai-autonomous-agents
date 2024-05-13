from math import dist
from typing import override
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao
from sae import Elemento


class ModeloMundo(ModeloPlan):

    """
    Corresponde às representações internas do ambiente. 
    A memoria é organizada internamente para poder ter a representação do domínio do problema.
    Na arquitetura deliberativa, o módulo de memória é indispensável e dá suporte à simulação interna.
    Qualquer sistema para poder antecipar o futuro, tem que ter conhecimento (modelo do mundo) (ou vem da experiencia ou vem de algo que já tem esse conhecimento e o transmite para o agente). Caso particular da representação do modelo do problema.
    Estende a classe ModeloPlan, que é uma classe abstrata que representa um modelo do mundo para um planeador deliberativo, de forma a não se comprometer a implementação deste modelo com um planeador específico.
    """
    
    def __init__(self):
        self.__estado = None
        self.__estados = [] # estados validos
        self.__elementos = {}
        self.__recolha = False # se um elemento foi recolhido então o ambiente foi alterado
    
    @override
    def obter_estado(self):
        return self.__estado

    @override
    def obter_estados(self):
        return self.__estados
    
    @override
    def obter_operadores(self):
        return [OperadorMover(self, direccao) for direccao in Direccao]
    
    def obter_elemento(self, estado):
        
        """
        Retorna o elemento associado à posicao de um estado.
        """

        # usar get para evitar erros, None é o valor por defeito
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):

        """
        Calcula a distância euclidiana entre a posição atual do agente e a nova posição.
        """

        nova_posicao = estado.posicao
        return dist(self.__estado.posicao, nova_posicao)
    
    def actualizar(self, percepcao):

        """
        Atualiza o modelo do mundo com a percepção que o agente obteve do ambiente.
        Atualizar, neste contexto, significa atualizar o estado do agente e os elementos que o rodeiam.
        """

        self.__estado = EstadoAgente(percepcao.posicao)
        self.__elementos = percepcao.elementos
        # representa um conjunto de posições válidas
        self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
        self.__recolha = percepcao.recolha
        
    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)

    @property
    def alterado(self):
        
        """
        Indica se o modelo do mundo foi alterado. Se um elemento alvo foi recolhido, então o ambiente foi alterado.
        """

        return self.__recolha
        