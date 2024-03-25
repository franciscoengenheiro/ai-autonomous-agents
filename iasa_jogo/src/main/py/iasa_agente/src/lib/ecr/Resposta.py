class Resposta:

    """
    Representa a geração de uma resposta a estímulos, inerentemente ligada a uma ação a ser executada e à sua respetiva prioridade.
    Várias respostas podes ser ativadas por uma única percepção. Além de poder ser ativada por um estímulo, uma resposta pode ser ativada também por uma percepção, de forma a garantir restrições de ativação (guardas)
    """
    def __init__(self, accao):
        self._accao = accao # protected attribute


    def activar(self, percepcao, intensidade = 0):

        """
        A ativação de uma resposta consiste em retornar a ação que a compõe, alterando a sua prioridade através do parâmetro intensidade. Se nenhuma intensidade for fornecida, a prioridade da ação baixa para a menor possível (0)
        """
        self._accao.prioridade = intensidade
        return self._accao
