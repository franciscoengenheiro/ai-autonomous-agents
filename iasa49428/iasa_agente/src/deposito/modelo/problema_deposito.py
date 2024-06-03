from deposito.modelo.estado_deposito import EstadoDeposito
from deposito.modelo.operadores.operador_encher import OperadorEncher
from deposito.modelo.operadores.operador_vazar import OperadorVazar
from mod.problema import Problema


class ProblemaDeposito(Problema):

    def __init__(self, valor_inicial, valor_final):
        self.__valor_final = valor_final
        volumes = [2, 3]
        operadoresEncher = [OperadorEncher(volume) for volume in volumes]
        operadoresVazar = [OperadorVazar(volume) for volume in volumes]
        operadores = operadoresEncher + operadoresVazar
        super().__init__(EstadoDeposito(valor_inicial), operadores)

    def objetivo(self, estado):
        return estado.volume == self.__valor_final
