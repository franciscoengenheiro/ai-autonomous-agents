"""

Inferência -> novas opções na resolução do problema tendo por base dados totalmente novos

Representações do domínio do problema

Processos de Codificação e Descodificação
- Codificação -> pegar numa informação concreta e transformar numa estrutura simbolica
- descodificar -> pegar numa estrutura simbolica e transformar em informação concreta

Modelo do problema:
- Estado é uma representação única simbolica de um conjunto de informações concretas

Raciocínio Automático com base em procura
Modelo do problema:
- estado: estrutura
- operador: dinâmico, gera a transição de um estado para outro

Problema: ciclos nos espaços de estados (i.e., estados repetidos)
Possibilidade de chegar ao mesmo estado por caminhos diferentes


Fator de ramificação, fator de expansão dos estados

- O estado objetivo é todo o estado que satisfaz a condição pretendida de um determinado problema

Problemas de Planeamento, consiste numa sequência de ações a realizar e de situações a percorrer para atingir uma situação final (objetivo), partindo de uma situação inicial

Processo de procura para cada estado:
1. Pegar no estado inicial 
2. aplicar operadores que geram as transições de um estado para outro
3. gerar novos estados (i.e., sucessores)
4. verificar se algum dos estados gerados é o estado objetivo
5. se não for, aplicar operadores aos estados sucessores

Fronteira do tipo LIFO (Last In First Out)

Arvore de procura:
- cada nó terá informação sobre:
  - estado
  - operador
  - Antecessor
  - Profundidade (i.e., nível do nó na árvore)
  - Custo (i.e., custo acumulado)

Processo de Procura
- As folhas da árvore, designados nós folha, são nós abertos e representam a fronteira da exploração
- Os nós já explorados são nós fechados porque já foram visitados

Métodos de Procura:
- Procura em profundidade (i.e., depth-first search): explorar os nós em profundidade primeiro
    - Remoção feita no início da fronteira
    - Nós mais recentes são colocados no início da fronteira

Procura termina quando:
- o nó objetivo é encontrado
- a fronteira está vazia, logo, não há solução

Hashable -> redefinem o hashcode e o equals, não usam o default (i.e., o endereço de memória)

Pode não existir estado sucessor, ou seja, o operador não gerou uma transição de estado dado o estado recebido

Procura em largura (i.e., breadth-first search): explorar os nós em largura primeiro, mais antigos primeiro. Fronteira do tipo FIFO (First In First Out), utiiliza a estrutura de explorados (abertos e fechados) para eliminar estados repetidos

Para definir uma solução ótima é necessário definir um critério de seleção, neste caso, o critério é o nr de passos

Critério de avaliação, custo, neste caso, para resolver o problema
de estados repetidos, o melhor nó é o que tem menor custo.

Modelar o problema:

Problema:
- estado inicial
- operadores
- função objetivo

Complexidade computacional: tempo (quanto tempo demora a encontrar a solução) e espaço (memoria) (quanta memória é necessária para produzir uma solução)

quanta memoria?
quanto tempo?

Arvore de Procura:

Factor de ramificação: número de sucessores de um nó (branching factor), b = 4
d = 1, nós processados = 1 + 4

Profundidade da procur (depth): nr de passos da raiz até ao nó

Complexidade temporal: O(b^d), onde b é o fator de ramificação e d é a profundidade da árvore, 

| procura      | complexidade espacial   | complexidade temporal |
|--------------|-------------------------|-----------------------|
| largura      | O(b^d)   exponencial    | O(b^d)    exponencial |
| profundidade | O(bd)    linear         | O(b^d)    exponencial |
| profundidade limitada | O(bd) linear    | O(b^d)    exponencial |

Cacteristicas dos metodos de procura:
- Completo: se existir solução, a solução é encontrada
- Ótimo: quando devolve uma solução é garantidamente a melhor solução
- Complexidade de espaço: quantos nos vao ser mantidos em memória
- Complexidade de tempo: quanto tempo demora a encontrar a solução

procura de profundidade, com limite de profundidade de procura: profundidade máxima que a procura pode atingir, tornando-se procura em largura após atingir o limite

como encontrar a profundidade?
- definir um limite de profundidade que vai sendo incrementado até encontrar a solução

1 - procura em profundidade
2 - procura em profundidade com limite de profundidade
3 - procura em profundidade iterativa, com profundidades incrementais

Procura melhor-primeiro
O nr de passos não reflete necessariamente a qualidade da solução
Associada a uma função de avaliação f, que avalia a qualidade de um nó (e.g., distância ao objetivo, tempo, custo)

Ordenar os nós na fronteira de acordo com a função de avaliação

Ordenação da fronteira ocorre quando é inserido um valor na fronteira.

Ter cuidado a eliminar os nós antigos porque os mais antigos podem ser melhores em relação ao custo associado

Procura de custo uniforme, funciona como a procura em largura, mas em vez de ordenar por profundidade, ordena por custo na fronteira. Caso particular da procura melhor-primeiro, onde a função de avaliação é o custo acumulado até ao nó

Se não tiver nos nós explorados ou se o custo do nó for menor que o custo do nó explorado, então o nó é inserido na fronteira

"""

class No:

    """
    Representa um nó de uma árvore de procura.
    É composto por um:
    - estado: estado que o nó representa
    - operador: operador que foi aplicado para gerar a transição do estado do nó para o estado sucessor
    - antecessor: nó antecessor ao qual foi aplicado o operador para gerar este nó
    - profundidade: profundidade do nó na árvore de procura (i.e., incremental a cada nível da árvore de procura)
    - custo: custo associado ao caminho que vai do nó raiz ao nó (i.e., incremental a cada transição de um nó para o nó sucessor)
    """

    def __init__(self, estado, operador = None, antecessor = None, custo = 0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__profundidade = 0
        if self.__antecessor is not None:
            self.__profundidade = self.__antecessor.profundidade + 1
        self.__custo = custo

    @property
    def custo(self):
        return self.__custo

    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor