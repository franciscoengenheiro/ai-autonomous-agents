from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao:
    
    def __init__(self, no_final):
        self.__no = no_final
        self.__passos = list(PassoSolucao(no_final.estado, no_final.operador))

    @property
    def custo(self):
        return self.__no.custo
    
    @property
    def dimensao(self):
        return len(self.__passos)
    
    # Semelhante ao <<Hashable>> do Estado on foi implementado o método __hash__ para que a solução possa ser usada como chave de um dicionário
    # mas agora para a solução <<Iterável>>
    def __iter__(self):
        return iter(self.__passos)