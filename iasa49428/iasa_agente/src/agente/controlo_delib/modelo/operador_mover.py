from math import cos, dist
from math import sin
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae import Accao

class OperadorMover(Operador):

    """
    Representação de um operador de movimento. Um operador de movimento é uma ação que gera uma transição de um estado para outro, sendo que a transição é a passagem de um estado para outro. O operador de movimento é caracterizado pela direção e passo.
    """

    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__accao = Accao(direccao)
    
    def aplicar(self, estado):

        """
        Gera a transformação de um estado para outro. Neste contexto, num ambiente bidimensional, a passagem de uma posição para outra é feita através de um passo e uma direção (translação geométrica). 
        """    

        angulo = self.__accao.ang
        passo = self.__accao.passo
        x, y = estado.posicao
        dx = round(passo * cos(angulo)) # arredondar para o inteiro mais próximo
        dy = round(-passo * sin(angulo)) # arredondar para o inteiro mais próxim
        nova_posicao = (x + dx, y + dy)
        estado_gerado = EstadoAgente(nova_posicao)
        if estado_gerado in self.__modelo_mundo.obter_estados():
            return estado_gerado
    
    def custo(self, estado, estado_suc):

        """
        Define o custo associado à transição de um estado para outro. Neste caso, o custo é a distância euclidiana entre as coordenadas (x, y) de dois pontos (posições).
        """

        return dist(estado.posicao, estado_suc.posicao)
    
    @property
    def ang(self):

        """
        Retorna o ângulo associado a accao.
        """

        return self.__accao.ang
    
    @property
    def accao(self):

        """
        Retorna a accao.
        """
        
        return self.__accao
    