class MecUtil:
    """
    Classe que implementa, através das equações de Bellman, o mecanismo de utilidade para calcular a Utilidade final.
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

        Composto por dois ciclos:
        - Ciclo exterior: termina quando a diferença entre a utilidade de um estado e a utilidade do estado anterior é menor que o delta máximo.
        - Ciclo interor: percorre todos os estados, calculando a utilidade de cada estado.
        """
        estados = self.__modelo.S()
        U = {estado: 0 for estado in estados}
        while True:
            Uanterior = U.copy()
            delta = 0
            for estado in estados:
                operadores = self.__modelo.A(estado)
                util_accoes = [
                    self.util_accao(estado, accao, Uanterior) for accao in operadores
                ]
                U[estado] = max(util_accoes, 0)
                delta = max(delta, abs(U[estado] - Uanterior[estado]))
            if delta <= self.__delta_max:
                break  # do while work around
        return U

    def util_accao(self, s, a, U):
        """
        U(s, a) = soma(T(s, a, s') * [R(s, a, s') + gama * U(s')])

        U(s') é a utilidade a longo prazo descontado pelo factor de desconto gama.

        Soma da probabilidade de transição de s para s' vezes a recompensa de s para s' mais gama vezes a utilidade de s'. Sendo s' um estado sucessor de s.
        """

        return sum(
            [
                self.__modelo.T(s, a, sn)
                * (self.__modelo.R(s, a, sn) 
                + self.__gama * U[sn])
                for sn in self.__modelo.S()
            ]
        )
