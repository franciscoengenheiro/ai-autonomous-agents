from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):

    """
    Mecanismo de procura informada (seletiva), que ao contrário da procura não informada, usa estratégias de exploração do espaço de estados que tiram partido de conhecimento do domínio do problema para ordenar a fronteira de exploração
    """

    def procurar(self, problema, heuristica):
        
        """
        Procura a solução para um problema de acordo com uma heurística, ou seja, baseada em conhecimento do domínio do problema.
        """
        
        self._avaliador.definir_heuristica(heuristica) # definição dinâmica da heurística
        return super().procurar(problema)
    