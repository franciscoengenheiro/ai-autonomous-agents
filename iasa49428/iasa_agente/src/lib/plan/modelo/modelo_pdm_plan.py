from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPDM, ModeloPlan):

    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan # usa fatorização por delegação
        self.__objectivos = objectivos
        self.__rmax = rmax
        # para o calculo ser mais rápido, pois está pre-calculado
        self.__transicoes = {
            # chave: estado, valor: {acção: estado}
            (s, a): a.aplicar(s)
            for s in self.obter_estados()
            for a in self.obter_operadores()
        }

    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    def S(self): 
        # compatiblidade com as bibliotecas
        return self.obter_estados()
    
    def A(self, s):
        # todos os operadores disponíveis se o estado não for um objectivo, caso contrário, retorna uma lista vazia (não há ações para esse estado)
        return self.obter_operadores() if s not in self.__objectivos else []
    
    def T(self, s, a, sn):
        # if a can be executed is 1, otherwise is 0 (deterministic ambient)
        return 1 if sn == self.__transicoes.get((s, a)) else 0
    
    def R(self, s, a, sn):
        # if the state is an objective, the reward is rmax, otherwise 0
        # n existe recompensa negativa porque os estados válidos não apresentam obstáculos
        return self.__rmax if sn in self.__objectivos else -a.custo(s, sn)
    
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else [] # se o ambiente for determinístico, retorna uma lista com um elemento. Se for ambiente não determinístico, poderá retornar mais do que um estado na lista