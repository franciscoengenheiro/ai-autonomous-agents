from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):

    """
    Representa um estímulo que corresponde à presença de um obstáculo numa determinada direção.
    A intensidade correspondente à distância ao obstáculo (i.e., intensidade 1 quando existe contacto com o obstáculo, intensidade 0 quando não existe obstáculo).
    """

    def __init__(self, direccao, intensidade : float = 1.0):
        self.__intensidade = intensidade
        self.__direccao = direccao
        

    def detectar(self, percepcao):
        if percepcao.contacto_obst(self.__direccao):
            return self.__intensidade
        else:
            return 0

        

        
        
    