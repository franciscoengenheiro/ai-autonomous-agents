from pee.mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """
    Fronteira do tipo FIFO (First In First Out), utilizada em problemas de procura em largura.
    """
    
    def inserir(self, no):
        """
        Insere um nó no final da fronteira.
        """
        self._nos.append(no)
        