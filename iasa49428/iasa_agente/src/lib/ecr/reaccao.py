from ecr.comportamento import Comportamento

class Reaccao(Comportamento):

    """
    Caracterizada como um comportamento simples é 
    responsável por definir, de forma modular associações (estimulo->resposta). Estas associações definem o comportamento do Agente, e que são acções diretamente atividadas em função das perceções do mesmo, sem necessidade de processamento adicional. (deliberação)
    """
    
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    """
    Ao estimulo inerente a esta reacção, é feita a deteção da percepção recebida. Se a intensidade do estimulo for superior a 0, é ativada a resposta associada a percepção e retornada a acção resultante, podendo ser uma acção sem efeito.
    """
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)
    
