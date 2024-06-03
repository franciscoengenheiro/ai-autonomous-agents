from deposito.modelo.estado_deposito import EstadoDeposito
from deposito.modelo.operadores.operador_transferir import OperadorTransferir

class OperadorVazar(OperadorTransferir):

    def __init__(self, volume):
        super().__init__(volume)
    
    def aplicar(self, estado):
        novo_volume = estado.volume - self._volume
        return EstadoDeposito(novo_volume) if novo_volume > 0 else EstadoDeposito(0)
    