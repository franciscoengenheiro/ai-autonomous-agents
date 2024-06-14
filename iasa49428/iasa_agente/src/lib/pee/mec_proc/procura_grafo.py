from typing import override
from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):

    """
    Representa um mecanismo de procura em grafo. Caracteriza-se por não explorar um nó se este já tiver sido explorado.
    """
    # codigo incremental
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {} # dicionário dos nós explorados

    def _memorizar(self, no):
        """
        Insere o nó na fronteira se o nó for para manter.
        """
        memorizar = self._manter(no)
        if memorizar:
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

    def _manter(self, no):
        """
        Indica se o nó é para manter ou não na fronteira. Se o nó já foi explorado, então não é para manter.
        """
        return no.estado not in self._explorados
    
    @override
    def get_max_nos_em_memoria(self):
        return len(self._explorados)
    
