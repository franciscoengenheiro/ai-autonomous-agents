from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao:

    """
    Representa uma solução de um problema de procura. Uma solução é composta por um nó final e por uma sequência de passos que conduzem do nó inicial ao nó final. Cada passo da solução é composto pelo estado do nó antecessor e pelo operador que conduz do estado do nó antecessor ao estado do nó atual.
    """

    def __init__(self, no_final):
        self.__no_final = no_final
        # EDIT: instead of: list(PassoSolucao(no_final.estado, no_final.operador)), use empty list
        self.__passos = []
        no = no_final
        # Iterar sobre os nós antecessores para construir a solução, recuando do nó final para o nó inicial até que não haja mais antecessores, construindo a solução passo a passo e inserindo à cabeça da lista de passos
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor

    @property
    def custo(self):
        return self.__no_final.custo
    
    @property
    def dimensao(self):
        # Edit: removes len() call to reduce time complexity
        return self.__no_final.profundidade
    
    # Semelhante ao <<Hashable>> do Estado onde foi implementado o método __hash__
    # para que a solução possa ser usada como chave de um dicionário
    # mas agora para a solução <<Iterable>> com o método __iter__
    def __iter__(self):
        return iter(self.__passos)
    
    # Permite aceder aos passos da solução como se fosse uma lista normal
    # sobrecarga do operadores
    def __getitem__(self, index):
        return self.__passos[index]