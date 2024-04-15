Inferencia -> novas opções na resolução do problema tendo por base dados totalmente novos

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

Modelar o problema