class Resposta:
    def __init__(self, accao):
        self.accao = accao
        
    def ativar(self, percepcao, intensidade : float = 0):
        raise NotImplementedError
