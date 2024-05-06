from math import dist
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from sae import Direccao


class ModeloMundo:

    """
    Corresponde às representações internas do ambiente. 
    A memoria é organizada internamente para poder ter a representação do domínio do problema.
    Na arquitetura deliberativa, o módulo de memória é indispensável e dá suporte à simulação interna.
    Qualquer sistema para poder antecipar o futuro tem que ter conhecimento (modelo do mundo) (ou vem da experiencia ou vem de algo que já tem esse conhecimento e o transmite para o agente). Caso particular da representação do modelo do problema.
    """
    
    def __init__(self):
        # Map from Elemento enum class 
        self.__estado = None
        self.__estados = []
        self.__operadores = []
        self.__elementos = {}
        self.__alterado = False
    
    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados
    
    def obter_operadores(self):
        return self.__operadores
    
    def obter_elemento(self, estado):
        
        """
        Retorna o elemento associado à posicao de um estado.
        """

        return self.__elementos[estado.posicao]
    
    def distancia(self, estado):
        posicao = estado.posicao
        # get euclidean distance between two points
        return dist(self.__estado.posicao, posicao)
    
    def actualizar(self, percepcao):

        """
        Atualiza o modelo do mundo com a percepção que o agente obteve do ambiente.
        Atualizar, neste contexto, significa atualizar o estado do agente, os elementos e as posições, bem como os operadores.
        """

        # percepcao.posicao
        # percepcao.elementos
        # percepcao.posicoes
        self.__alterado = self.__foi_alterado(percepcao)
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__elementos = percepcao.elementos
        for posicao in percepcao.posicoes: # posições válidas
            self.__estados.append(EstadoAgente(posicao))
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        
    def mostrar(self, vista):
        raise NotImplementedError("Por implementar")

    def __foi_alterado(self, percepcao):

        """
        Verifica se o modelo do mundo foi alterado.
        """

        if self.__estado is None:
            return False
        else:
            # TODO: estados mudar para posicoes: self.__estados != percepcao.posicoes
            return self.__estado.posicao != percepcao.posicao or self.__elementos != percepcao.elementos or self.__estados != percepcao.posicoes

    @property
    def alterado(self):
        return self.__alterado
        