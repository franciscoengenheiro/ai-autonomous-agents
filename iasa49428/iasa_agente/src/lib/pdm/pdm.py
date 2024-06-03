from pdm.mec_util import MecUtil


class PDM():

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):

        """
        Calcula a política óptima (π*) com base na utilidade de cada acção (maximiza a utilidade esperada)
        π*(𝑠) = 𝑎𝑟𝑔𝑚𝑎𝑥 𝑎 𝑈(𝑠, 𝑎)
        pol(s) = a

        U(s, a) = soma(T(s, a, s') * [R(s, a, s') + gama * U(s')])
        
        Escolher a acção que tem a maior utilidade
        Usar a função util_accao para calcular a utilidade de cada acção
        O argmax é o valor que conseguimos maximizar. 
        Pedimos ao max que o conjunto de elementos A, ir analisá-los todos, verificar no parâmetro key que é uma função lambda que irá  verificar esse elemento.
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
        
        # resolver o problema de decisão de Markov
        # devolve a utilidade final e a política
        Ufinal = self.__mec_util.utilidade()
        politica = self.politica(Ufinal)
        return Ufinal, politica
        