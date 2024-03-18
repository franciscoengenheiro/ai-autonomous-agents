class Resposta:
    """
    Encapsula a resposta a uma percepção, inerentemente ligada a uma ação a ser executada e à sua respetiva prioridade.
    Várias respostas podes ser ativas por uma única percepção, sendo que esta é um agregado de estímulos.
    Uma resposta pode ser ativada por um estímulo ou pela perceção, de forma a garantir guardas de ativação.
    """
    def __init__(self, accao):
        self._accao = accao # protected attribute


    def ativar(self, percepcao, intensidade : float = 0):
        """
        A ativação de uma reposta consiste em retornar a ação que a compõe, alterando a sua prioridade através do parâmetro intensidade. Se nenhuma intensidade for fornecida, a prioridade da ação baixa para 0.
        """ 
        self._accao.prioridade = intensidade
        return self._accao
