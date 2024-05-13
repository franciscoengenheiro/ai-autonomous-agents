from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae import Controlo

class ControloDelib(Controlo):

    """
    Corresponde a um componente que exerce raciocínio automático, mais concretamente, prático (orientado para a ação - interação permanente com o mundo, ao qual está associado o processo de tomada de decisão)
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
    Sequencia de ações -> Planos de ação: vão caracterizar o comportamento do agente e não as reações, pelos quais os agentes vão passar para atingir os objetivos.
    """

    def __init__(self, planeador):
        self.__planeador = planeador
        modelo_mundo = ModeloMundo()
        self.__modelo_mundo = modelo_mundo
        self.__mecdelib = MecDelib(modelo_mundo)
        self.__objetivos = None
        self.__plano = None # plano a executar   

    def processar(self, percepcao):

        """
        Processo da tomada de decisão do agente:
        1. Nota: SAE faz a observação do mundo (geração de perceções), e portanto esse passo é omitido nesta implementação.
        2. Atualizar o modelo do mundo
        3. Se for necessário reconsiderar:
        4.    Deliberar
        5.    Planear
        6. Executar o plano de acção
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.__mostrar()
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

        return not self.__plano or self.__modelo_mundo.alterado

    def __deliberar(self):

        """
        Significa ponderar alternativas e escolher a melhor opção. Neste caso, a melhor opção é a que leva o agente a atingir os objetivos. 
        Este método é delegado ao mecanismo deliberativo. 
        Faz parte do processo de tomada de decisão, nomeadamente, depois de uma reconsideração.
        """

        self.__objetivos = self.__mecdelib.deliberar()
    
    def __planear(self):

        """
        Planeia a sequência de ações que o agente deve executar para atingir os objetivos. 
        Este método é delegado ao planeador.
        Faz parte do processo de tomada de decisão, nomeadamente, depois de uma reconsideração, mais concretamente, depois de deliberar.
        """

        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
    
    def __executar(self):

        """
        Executa o plano de ação. Se o plano existir, então o agente executa a próxima ação do plano, caso contrário, o plano está dessincronizado (i.e., o estado atual do agente não é compátivel com o estado do passo solução) com o modelo do mundo e por isso é necessário descartar o plano.
        """   

        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None
    
    def __mostrar(self):

        """
        Mostra o modelo do mundo e o plano de ação.
        """

        # Para não acumular informação na consola
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano: 
            # Mostrar o plano
            self.__plano.mostrar(self.vista)
        if self.__objetivos:
            # Mostrar os objetivos
            for objetivo in self.__objetivos:
                self.vista.marcar_posicao(objetivo.posicao)