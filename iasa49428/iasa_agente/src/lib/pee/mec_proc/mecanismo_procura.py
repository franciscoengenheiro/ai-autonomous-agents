from abc import ABC, abstractmethod
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

class MecanismoProcura(ABC):

    """
    Mecanismo de procura genérico que permite abstrair a forma como a procura é feita, não estando portanto, comprometido com a implementação do algoritmo de procura.
    """

    def __init__(self, fronteira):
        self._fronteira = fronteira
        self.__nos_processados = 0
        self.__max_nos_em_memoria = 0

    def _iniciar_memoria(self):

        """
        Neste contexto, iniciar a memória significa garantir que a estrutura de dados que representa os elementos iniciais da fronteira está inicializada.
        """

        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        """
        Permite abstrair a forma como o nó é memorizado sem se comprometer com a implementação do algoritmo de procura.
        Inicial:
        BFS:
        - Inserir na Fronteira com LIFO (Last In First Out)
        DFS:
        - Inserir na Fronteira com FIFO (First In First Out)
        - Procurar no dicionário dos nós explorados (fronteira de exploração, nós gerados mas não expandidos, abertos + nós expandidos, fechados) se o nó já foi explorado

        No passo da expansão de cada nó:
        BFS:
        - O nó sucessor é inserido na fronteira de exploração
        DFS:
        - Se o estado do nó sucessor não está no dicionário dos nós explorados, então o nó sucessor é inserido na fronteira de exploração e posteriomente adicionado ao dicionário
        """

    def procurar(self, problema):

        """
        Define o comportamento abstrato de um mecanismo de procura.
        Processo de procura para cada estado:
        1. Criar um nó para representar o estado inicial
        2. Memorizar o nó (vai depender da estratégia de procura - ver método _memorizar)
        3. Enquanto a fronteira não estiver vazia
            4. Remover um nó da fronteira
            5. Verificar se o estado que lhe está associado é um estado objetivo, se sim, sair, devolvendo a solução que contém esse nó
            6. Expandir o nó removido tendo em conta o problema, gerando os nós sucessores
            7. Memorizar os nós sucessores (vai depender da estratégia de procura - ver método _memorizar)
        """

        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        self.__nos_processados = 0
        self.__max_nos_em_memoria = 1
        while not self._fronteira.vazia:
            no = self._fronteira.remover()

            # Atualizar a contagem de nós processados
            self.__nos_processados += 1

            if problema.objetivo(no.estado):
                return Solucao(no)
            nos_sucessores = self._expandir(problema, no)
            for no_sucessor in nos_sucessores:
                self._memorizar(no_sucessor)
                self.__max_nos_em_memoria = max(self.__max_nos_em_memoria, self._fronteira.dimensao)

    def _expandir(self, problema, no):

        """
        Expandir um nó, tendo em conta o problema que se pretende resolver, tem associados os seguintes passos:
        1. Para cada operador gerar a transição de estado do nó, que vai permitir obter o estado sucessor
        2. Se o estado sucessor existir:
            3. Calcular o custo do nó sucessor (custo do nó antecessor + custo da transição para o estado sucessor);
            4. Criar o nó sucessor com o estado sucessor, o operador que gerou a transição, o nó antecessor e o custo calculado
            5. Guardar o nó sucessor na lista de sucessores
        6. Devolver a lista de sucessores
        """

        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(estado)
            if estado_sucessor is not None:
                custo = no.custo + operador.custo(estado, estado_sucessor)
                no_sucessor = No(estado_sucessor, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
    
    def get_nos_processados(self):
        return self.__nos_processados

    def get_max_nos_em_memoria(self):
        return self.__max_nos_em_memoria
