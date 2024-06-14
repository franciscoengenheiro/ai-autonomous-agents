from mod.estado import Estado

class EstadoPuzzle(Estado):

    """
    Representa a informação sobre a configuração de um tabuleiro de jogo.
    @param config: lista de inteiros que representam a configuração do tabuleiro
    """

    def __init__(self, config):
        self.__config = config

    def id_valor(self):
        sum = 0
        for i in range(0, len(self.__config)):
            sum += self.__obter_cod_base10(i)
        return sum

    def __obter_cod_base10(self, numero):

        """
        Retorna o valor do número na base 10.
        """

        # means: self.__config[i] * 10^i
        return self.__config[numero] * (10 ** numero)