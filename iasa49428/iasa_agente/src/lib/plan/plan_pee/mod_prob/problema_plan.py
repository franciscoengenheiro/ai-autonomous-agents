from mod.problema import Problema


class ProblemaPlan(Problema):

    """
    TODO
    """

    def __init__(self, modelo_plan, estado_final):
        # obter estado inicial de forma dinamica e a partir daí obter operadores
        estado_inicial = modelo_plan.obter_estado()
        operadores = modelo_plan.obter_operadores()
        self.__estado_final = estado_final
        super().__init__(estado_inicial, operadores)
    
    def objetivo(self, estado):

        """
        TODO
        """

        return estado == self.__estado_final
