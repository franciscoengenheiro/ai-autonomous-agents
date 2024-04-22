from pee.mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """
    Fronteira do tipo LIFO (Last In First Out), utilizada em problemas de procura em profundidade.
    """
    
    def inserir(self, no):
        """
        Insere um nó no início da fronteira.
        """
        self._nos.insert(0, no)
        