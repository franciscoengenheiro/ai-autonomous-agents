from sae import Controlo

class ControloReact(Controlo):

    """
    Define o controlo de uma arquitetura reativa simples.
    Nesta arquitetura, as ações são ativadas diretamente em função das perceções do Agente, sem necessidade de processamento adicional (deliberação) ou representações internas do estado do mundo.
    """
    
    def __init__(self, comportamento):
        self.__comportamento = comportamento
        self.mostrar_per_dir = True # permite mostrar na segunda janela do ambiente de simulação a perceção e a direção do agente

    def processar(self, percepcao):
        """
        Retorna a ação resultante da ativação do comportamento associado a este controlo reativo. A ativação do comportamento é realizada com base na perceção recebida.
        """
        
        return self.__comportamento.activar(percepcao)
    