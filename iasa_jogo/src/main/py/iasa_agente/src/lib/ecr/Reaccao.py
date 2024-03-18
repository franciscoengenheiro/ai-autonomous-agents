from . import Comportamento

class Reaccao(Comportamento):

    """
    Caracterizada como um comportamento simples.
    Responsável por definir, de forma modular associações (estimulo->resposta), que definem o comportamento do Agente, e que são acções diretamente atividadas em função das perceções do mesmo, sem necessidade de processamento adicional. (deliberação)
    """
    
    def __init__(self, estimulo, resposta):
        # a = A(); a.m1("teste") translates to A.m1(a, "tests")
        # self.a1 = NONE (ausência de valor, NULL?)
        # __ significa que o atributo é privado
        # _  significa que o atributo é protegido
        #    significa que o atributo é público
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    """
    Ao estimulo inerente a esta reacção, é feita a deteção da percepção recebida. Se a intensidade do estimulo for superior a 0, é ativada a resposta associada a percepção e retorna a acção resultante
    """
    def ativar(self, percepcao):
        # pass # equals no-op
        # raise NotImplementedError
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            accao = self.__resposta.ativar(percepcao, intensidade)

        return accao
