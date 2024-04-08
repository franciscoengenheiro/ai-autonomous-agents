
from random import choice
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae.agente.accao import Accao
from sae.ambiente.direccao import Direccao

class RespostaEvitar(RespostaMover):

    """
    Representa a resposta de um agente para evitar um obstáculo.
    """
    def __init__(self, dir_inicial : Direccao = Direccao.ESTE):
        self.__direccoes = list(Direccao)
        super().__init__(dir_inicial)

    def activar(self, percepcao, intensidade):
        # Edit: self.__direccao -> self._accao.direccao, para poder aceder à direção da ação
        # associada de forma protegida
        # existe um obstáculo na direção atual?
        if percepcao.contacto_obst(self._accao.direccao):
            # procurar uma direção livre
            direccao_livre = self.__direccao_livre(percepcao)
            # Se houver uma direção livre:
            # - mudar a ação para se mover na nova direção
            # - retornar a ação
            if direccao_livre:
                # Edit: self._accao(direccao_livre) -> self._accao.direccao = direccao_livre
                # visto que accao não é um método, mas sim uma propriedade com campos
                self._accao.direccao = direccao_livre
                return super().activar(percepcao, intensidade)
            else:
                # Se não houver direção livre, a ação é nula
                return None
            
        # Se não houver obstáculo na direção atual, a ação é a mesma
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):

        """
        Retorna a primeira direção livre, ou seja, sem obstáculos.
        """

        # Edit: foi alterado a implementação deste método para usar list comprehension
        dir_livres = [direccao for direccao in self.__direccoes if not(percepcao.contacto_obst(direccao))]
        if dir_livres:
            return choice(dir_livres) 
    
        