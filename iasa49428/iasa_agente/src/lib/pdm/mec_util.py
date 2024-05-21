class MecUtil():

    """
    Responsável pelo cáculo da utilidade.
    Utilidade é um dicionário, cuja chave é um estado, e o valor é um double.

    """

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__delta_max = delta_max
        self.__gama = gama
    
    def utilidade(self):

        """
        Calcula a utilidade para cada estado com base na equação de Bellman. 
        A utilidade desse estado tem que ser ponderada com a utilidade dos estados seguintes, de forma a maximizar a utilidade da acção a escolher.

        U(s) = max(a) soma(T(s, a, s') * (R(s, a, s') + gama * U(s'))), para cada s pertencente a S.
        """    
        estados = self.__modelo.S()
        U = {estado: 0 for estado in estados}
        while True:
            Uanterior = U.copy()
            delta_currente = 0
            for estado in estados:
                operadores = self.__modelo.A(estado)
                util_accoes = [self.util_accao(estado, accao, Uanterior) for accao in operadores]
                U[estado] = max(util_accoes)
                novo_delta = abs(U[estado] - Uanterior[estado])
                delta_currente = max(delta_currente, novo_delta)
            if delta_currente < self.__delta_max:
                break # do while work around
        return U

    def util_accao(self, s, a, U):

        """
        U(s, a) = soma(T(s, a, s') * (R(s, a, s') + gama * U(s')))

        Soma da probabilidade de transição de s para s' vezes a recompensa de s para s' mais gama vezes a utilidade de s'. Sendo s' um estado sucessor de s.
        """    

        raise NotImplementedError("Not implemented yet")

