from sae import Controlo

class ControloReact(Controlo):

    """
    Define o controlo de uma arquitetura reativa simples denominada ecr (estímulo->comportamento->resposta), onde as acoes são diretamente ativadas em função das perceções do agente, sem necessidade de processamento adicional (deliberação).
    """

    def __init__(self, comportamento):
        self.__comportamento = comportamento


    def processar(self, percepcao):

        """
        Ativa a percepcão recebida associada ao comportamento inerenete ao controlo reativo e retorna a ação resultante.
        """
        return self.__comportamento.ativar(percepcao)