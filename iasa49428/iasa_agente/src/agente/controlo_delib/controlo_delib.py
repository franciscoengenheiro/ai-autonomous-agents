from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae import Controlo

class ControloDeliberativo(Controlo):

    """
    Corresponde a um componente que exerce raciocínio automático, mais concretamente, prático (orientado para a ação - interação premanente com o mundo, ao qual está associado o processo de tomada de decisão)
    Está inserido numa arquitetura deliberativa, que é uma arquitetura de controlo de agentes que se baseia na deliberação, ou seja, na ponderação de alternativas e na escolha da melhor opção. Além daquilo que a arquitetura reativa faz (presente e passado), a deliberativa é capaz de planear e antecipar (futuro).
    Input:
    - objetivos a atingir
    - ações realizáveis
    - representação do mundo
    Output:
    - Planos de ação
    Apresenta 2 vertentes:
    - Raciocinio sobre fins (deliberativo) - opções -> objetivos
    - Raciocinio sobre meios (planeamento) - ações -> planos
    Sequencia de ações -> Planos de ação -> Vão caracterizar o comportamento do agente e não as reações, pelos quais os agentes vão passar para atingir os objetivos.
    """

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__mecdelib = MecDelib()
        self.__modelo_mundo = ModeloMundo()
        self.__objetivos = None
        self.__plano = None # plano a executar
        raise NotImplementedError("Por implementar")    

    def processar(self, percepcao):

        """
        Processo da tomada de decisão do agente:
        1. Nota: SAE faz a observação do mundo (geração de perceções), e portanto esse passo não é necessário nesta fase.
        2. Atualizar o modelo do mundo
        3. Se for necessário reconsiderar:
        4.    Deliberar
        5.    Planear
        6. Executa o plano de acção
        """
        self.__assimilar(percepcao)
        reconsiderar = self.__reconsiderar()
        if reconsiderar:
            self.__deliberar()
            self.__planear()
        accao = self.__executar()
        return accao
    
    def __assimilar(self, percepcao):

        """
        Atualiza o modelo do mundo com a percepção que o agente obteve do ambiente.
        """

        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):

        """
        Se o plano não existir ou o modelo do mundo foi alterado, então é necessário reconsiderar.
        """

        if self.__plano is None or self.__modelo_mundo.alterado:
            return True

    def __deliberar(self):

        """
        Significa ponderar alternativas e escolher a melhor opção. Neste caso, a melhor opção é a que leva o agente a atingir os objetivos. Este método é delegado ao mecanismo deliberativo. Faz parte do processo de tomada de decisão, nomeadamente, depois de uma reconsideração.
        """

        objetivos = self.__mecdelib.deliberar()
        self.__objetivos = objetivos
    
    def __planear(self):

        """
        Planeia a sequência de ações que o agente deve executar para atingir os objetivos. Este método é delegado ao planeador. Faz parte do processo de tomada de decisão, nomeadamente, depois de uma reconsideração.
        """

        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
    
    def __executar(self):

        """
        Executa o plano de ação. Se o plano existir, então o agente executa a próxima ação do plano.
        """   

        if self.__plano is not None:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            accao = operador.accao
            if accao is not None:
                return accao
    
    def __mostrar(self):
        self.__plano.mostrar(self.vista)
        self.__modelo_mundo.mostrar(self.vista)