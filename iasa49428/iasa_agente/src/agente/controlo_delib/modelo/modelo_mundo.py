from math import dist
from typing import override
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao


class ModeloMundo(ModeloPlan):

    """
    Corresponde às representações internas do ambiente. 
    A memoria é organizada internamente para poder ter a representação do domínio do problema.
    Na arquitetura deliberativa, o módulo de memória é indispensável e dá suporte à simulação interna.
    Qualquer sistema para poder antecipar o futuro, tem que ter conhecimento (modelo do mundo) (ou vem da experiencia ou vem de algo que já tem esse conhecimento e o transmite para o agente). Caso particular da representação do modelo do problema.
    """
    
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__operadores = []
        self.__elementos = {}
        self.__alterado = False
    
    @override
    def obter_estado(self):
        return self.__estado

    @override
    def obter_estados(self):
        return self.__estados
    
    @override
    def obter_operadores(self):
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        return self.__operadores
    
    def obter_elemento(self, estado):
        
        """
        Retorna o elemento associado à posicao de um estado.
        """

        return self.__elementos[estado.posicao]
    
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

        # percepcao.posicao
        # percepcao.elementos
        # percepcao.posicoes
        novo_estado = EstadoAgente(percepcao.posicao)
        if novo_estado != self.__estado: # comparar estados (aka posições)
            self.__estado = novo_estado
            self.__elementos = percepcao.elementos
            for posicao_valida in percepcao.posicoes: # representa um conjunto de posições válidas
                self.__estados.append(EstadoAgente(posicao_valida))
            self.__alterado = True
        else:
            self.__alterado = False
        
    def mostrar(self, vista):
        raise NotImplementedError("Por implementar")

    @property
    def alterado(self):
        
        """
        Indica se o modelo do mundo foi alterado.
        """

        return self.__alterado
        