from sae import Controlo

class ControloReact(Controlo):

    """
    Define o controlo de uma arquitetura reativa simples denominada ecr: estímulo->comportamento->resposta. Nesta arquitetura, as acoes são ativadas diretamente em função das perceções do Agente, sem necessidade de processamento adicional (deliberação) ou representações internas do estado do mundo.
    """
    
    def __init__(self, comportamento):
        self.__comportamento = comportamento

    def processar(self, percepcao):

        """
        Retorna a ação resultante da ativação do comportamento associado a este controlo reativo. A ativação do comportamento é realizada com base na perceção recebida.
        """
        return self.__comportamento.ativar(percepcao)
    