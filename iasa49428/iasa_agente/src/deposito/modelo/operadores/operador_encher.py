from deposito.modelo.estado_deposito import EstadoDeposito
from deposito.modelo.operadores.operador_transferir import OperadorTransferir

class OperadorEncher(OperadorTransferir):

    def __init__(self, volume):
        super().__init__(volume)
    
    def aplicar(self, estado):
        return EstadoDeposito(estado.volume + self._volume)
    