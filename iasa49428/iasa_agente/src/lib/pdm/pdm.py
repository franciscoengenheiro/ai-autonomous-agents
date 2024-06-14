from pdm.mec_util import MecUtil


class PDM():

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):

        """
        Calcula a política óptima (π*) com base na utilidade estimada (U) para cada estado mediante uma acção.
        π*(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥 𝑎 𝑈(𝑠, 𝑎)
        pol(s) = max(A, key = lambda a: U(s,a)), sendo A o conjunto de acções possíveis num estado s
        U(s, a) = soma(T(s, a, s') * [R(s, a, s') + gama * U(s')]), para cada estado sucessor s' de s
        """
        politica = {}
        estados = self.__modelo.S()
        for estado in estados:
            operadores = self.__modelo.A(estado)
            # pol[s] = max(A, key = lambda a: U(s,a))
            if operadores:
                politica[estado] = max(operadores, key = lambda a: self.__mec_util.util_accao(estado, a, U), default=0)
        return politica
    
    def resolver(self):

        """
        Resolve o problema de decisão de Markov: 
        - Calcula a utilidade final
        - Calcula a política óptima com base na utilidade final
        Retorna essa informação
        """
        
        Ufinal = self.__mec_util.utilidade()
        politica = self.politica(Ufinal)
        return Ufinal, politica
        