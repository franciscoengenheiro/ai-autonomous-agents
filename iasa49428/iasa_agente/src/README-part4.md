Memoria e comportamento

Agentes Reativos: atual (presente)
Agentes Reativos com Estado: prever (passado) e atual (presente)
Agentes deliberativos: prever (passado) e antecipar (futuro)

Passado: Repetir/evitar
Presente: Reagir
Futuro: Antecipar

Processo deliberativo: processo em que o agente intencionalmente, com o proposito de atingir um determinado objetivo, simula as situações futuras, avalia as consequências de suas ações e escolhe a melhor ação a ser tomada.

Na arquitetura deliberativa, o módulo de memória é indispensável e dá suporte à simulação interna. Processos internos -> planos de ação (o sistema por simulação interna vai)

Sequencia de ações -> Planos de ação -> Vão caracterizar o comportamento do agente e não as reações. Pelos quais os agentes vão passar para atingir os objetivos.

Conceito: Sistemas intencionais (operam por concretização de intenções)

Objetivos explicitos, ao contrário dos reativos que são implícitos. Os objetivos são explicitos e são a base para a tomada de decisão.

geração dos objetivos: processo computacional - deliberação
SLIDE 8 (usar o desenho no projeto)

Qualquer sistema para poder antecipar o futuro tem que ter conhecimento (modelo do mundo) (ou vem da experiencia ou vem de algo que já tem esse conhecimento e o transmite para o agente). Caso particular da representação do modelo do problema.

consegue simular para cada opção as multiplas, quais as sequencias de evolução possíveis. (simulação interna)

Racicionio Automático: Dividido em 2 partes:

- Prático: orientado para a ação (interação premanente com o mundo, ao qual está associado o processo de tomada de decisão)
  Input:
  - objetivos a atingir
  - ações realizáveis
  - representação do mundo
    Output:
  - Planos de ação
- Teórico: orientado para o conhecimento, direto

Raciocionio Prático: 2 vertentes:

- Raciocinio sobre fins (deliberativo) - opções (input) -> objetivos (output)
- Raciocinio sobre meios (planeamento) - ações (input) -> planos (output)

Racionalidade Limitada -> O agente tenta chegar uma solução satisfatória, não a melhor solução, de forma dinâmica. Tendo por base os recursos computacionais disponiveis.

Memoria é organizada internamente para poder ter a representação do domino do problema. (modelo do mundo)

processo da tomada de decisão:

1. observar o mundo e gerar perceções
2. atualizar o conhecimento interno, gerando perceções
3. deliberar sobre os objetivos a atingir antes de planear
4. planear ações para atingir os objetivos
5. executar o plano de ação

Conceito de Reconsideração: O mundo alterou-se e tem impacto nos objetivos do agente? Agrega
deliberar e planear. (reconsiderar os objetivos e planos de ação)

ALTERAÇÃO NO MODELO do mundo -> necessário para o processo de reconsideração

Planeadores tem que ser compativeis, pois vão representar ambientes estáticos e dinâmicos.

Plano é uma sequencia de ações que o agente tem que executar para atingir um determinado objetivo, ao qual é possivel consultar por estado e obter o operador

é uma metrica

O PLANO PODE ALTERAR CONSOANTE O TEMPO (ANALOGIA, CAMIAO QUE SEGUIA UM TRAJETO MAS POR CAUSA DE AREIA NO CAMINHO TEVE QUE ALTERAR O TRAJETO)

IMPORTANTE: !! FOR ALTERADO NO PLANO pee E NÃO vai ser implementado o metodo valido nem vai ser usada a propriedade solução.

20/05/2024

Processos de Decisão Sequencial:

Conjunto de operadores: determina o conjunto de ações que o agente pode executar

Problema:
- valor estar diferido no tempo (incerto)
- existir incerteza no mundo

A incerteza resulta da impossibilidade de se obter informação completa relativa ao domínio do problema (e.g., navegação em veículos autónomos).
A incerteza traduz-se no facto de o sistema quando vai tomar a decisão, toma uma decisão não deterministica (probabilistica, com uma determinada probabilidade de sucesso), pois não tem informação completa do mundo para afirmar, com certeza, que a decisão tomada é a melhor quando comparada com outras possiveis.

Por simulação daquilo que pode acontecer, o sisteam consegue antecipar, através do raciocinio automático, o que pode acontecer. Sem incerteza e sabendo o que pode acontecer, o agente consegue tomar a melhor desisão a partir de um plano de ação. No caso geral, 

O valor (utilidade) tem haver com o efeito acumulativo que vai tendo do mundo, através dos ganhos e perdas que vai tendo, diferido no tempo. (e.g., no mercado financeiro, o valor de uma ação é volatil e varia ao longo do tempo, ganhar ou perder dinheiro (recompensa diferida)). Poderão existir estados em que não existem ganhos e perdas. Utilidade representa o valor de se estar num estado, para efeito de concretização de um objetivos do sistema, mas representa o valor a longo prazo (na história de evolução do sistema) (e.g., um automóvel pode ter que acelarar, gastando mais combustivel, para evitar um acidente, mas a longo prazo, o valor de evitar o acidente é maior do que o valor de gastar mais combustivel).

Processos de decisão sequencial:

Em contraste com um planeador, onde se só tinha em conta o custo, agora temos em conta a estes fatores.

– Utilidade de uma acção depende de uma sequência de decisões
– Possibilidade de ganhos e perdas
– Incerteza na decisão
– Efeito cumulativo

A arquitetura de espaços de estados é deterministica, onde toda a informação é conhecida e não existe ambiguidade (todas as transições de estado são definidas no sistema)

A arquitetura de espaços de estados deterministica ?
O agente pode permancer no mesmo estado ou mudar de estado, dependendo da ação que foi tomada, associada a uma probabilidade de sucesso e a uma possível recompensa (positiva, negativa, ou nula, no contexto local). A soma das várias probabilidades de cada ação tem que ser igual a 1.

Propriedade de Markov, é um dos ramos no espaço de estados, ou seja, é uma sequência de evolução de estados futuros que podem acontecer.

A evolução futura de estado, incluindo incerteza e recemponsa, só depende do estado atual e não de estados anterior. (processos de decisão de markov, processo de decisão sequencial, e se o contexto é que essa decisão tomada garante a propriedade de markov, então é um processo de decisão de markov)

Fatores importantes no processo de decisão de markov:
- S – conjunto de estados do mundo
- Modelo de transição que dá informação sobre a probabilidade de mudaça de estado (T(s, a, s’), onde s é o estado atual, a é a ação a ser tomada, e s’ é o estado futuro, e T(s, a, s’) é a probabilidade de mudança de estado de s para s’, após a ação a ser tomada)
- Modelo de recompensa (R(s, a, s’), onde s é o estado atual, a é a ação a ser tomada, e s’ é o estado futuro, e R(s, a, s’) é a recompensa associada à transição de estado de s para s’, após a ação a ser tomada)
- Factores de desconto (γ, onde 0 <= γ <= 1, que é o fator de desconto, que é aplicado à recompensa. Por cada unidade de tempo que passa, a recompensa é descontada por um fator de γ, que é o fator de desconto, de forma exponencial). Na realidade é um fator de retensão, ou seja, o valor da recompensa é retido ao longo do tempo, e é descontado por um fator de γ, que é o fator de desconto, de forma exponencial (y = 0.5, retem-se 50% do valor da recompensa, e desconta-se 50% do valor da recompensa, por cada unidade de tempo que passa). Se o gama for zero, a tomada de decisão só depende do presente, porque o futuro é anulado.
- Cadeia de markov

Para o contexto humano, 

Não é possível fazer raciocinio ótimo mas sim automático, devido à racionalidade limitada.


Perda de Oportunidade na passagem do tempo, recompensas descontadas no tempo

principio da decisão ótima, é aquela que maximima a utilidade esperada (informação em cada estado, slide 10 - 15). 

Se é possível, calcular a utilidade esperada, então é possível calcular a decisão ótima. Politica (estratégia da tomada de decisão, conjunto de ações, é uma função que indica para cada estado, qual é a ação que deve ser realizada) (e.g., calculo da politica de seguro (exemplo), maximizar a utilidade esperada, e a politica de seguro é a sequência de ações que maximiza a utilidade esperada).

A politica é uma função que indica para cada estado, qual é a ação que deve ser realizada.

O conceito matemático de função, que associa elementos de dois dominios, dominio e contra dominio.
Politica o dominio é o conjunto de estados, e o contra dominio é o conjunto de ações.

S = {s0, s1, s2}
politica : S -> A(s)

politica(s: S) : A(s)

Produto Cartesiano:
A = {a1, a2}
S = {b1, b2}

A x S = {(a1, b1), (a1, b2), (a2, b1), (a2, b2)}

politica: SxA -> [0, 1]

politica(s: S, a: A) : [0, 1]
politica(s0, a0) = 0.3
politica(s0, a1) = 0.5
politica(s0, a2) = 0.2

slide 12 - 15:
Politica Deterministica
pol((1, 1)) = NORTE
pol((2, 1)) = OESTE 
pol((3, 1)) = NORTE
pol((4, 1)) = OESTE

Politica Não Deterministica
pol((1, 1), NORTE) = 0.3

r = -1             p = 0.8
r = -10 (colisão)  p = 0.1
r = -10 (colisão)  p = 0.1

R = -1*0.8 + -10*0.1 + -10*0.1 =
  = -0.8 - 1 - 1 = -2.8 (ponderação das várias hipoteses)

Auto semelhança, recursividade.

U(s) = r1 + g*r2 + gama^2*r3 + gama^3*r4 + ... + gama^n*rn
U(s') = r2 + g*r3 + ....
U(s) = r1 + g*U(s')
recompensa + gama * recompensas dos estados seguintes

O agente tem um plano, mas ações são não deterministicas, e o agente tem que escolher a ação que maximiza a utilidade esperada.

Recompensa de -1, para considerar o gasto de energia, se houver colisão (esquerda ou direita) existe uma perda de -10 (por exemplo) A recompensa não é deterministica no estado, mas sim não deterministica.

Equação de Bellman (essencia do raciocinio), corresponde ao principio da decisão ótima, que é a que maximiza a utilidade esperada.
U(s) = ?
A utilitidade de um estado é a recompença mais game*U(s') (onde s' é o estado futuro, e U(s') é a utilidade do estado futuro, e gama é o fator de desconto, que é aplicado à recompensa, de forma exponencial, por cada unidade de tempo que passa).

pol(s) = argmax(a, U(s, a))

max([2, 5, 1, 7, 3]) = 7
f(x) = 2*x, x < 10

max(f(x)) = 18
argmax(x, f(x)) = 9

pol[s] = max(A, key=lambda a: U(s, a)) // argmax

U(s, a) = soma(s', T(s, a, s') * (R(s, a, s') + gama*U(s')))
U(s) = soma(a, pol(s,a) * U(s, a)), a utilidade de um estado é a soma da probablidade de escolher uma ação multiplificada plea utilidade do estado seguinte

Transformar a recursividade em iteratividade (guardando soluções intermédias) Teoria da programação dinamica

algoritmo: utilidade a zero para todos os estados, a exceção do sitio onde estão as recompenas, para cada estado vai ser calculada a utilidade, tendo por base a utilidade anterior

conjunto de estados
conjunto de ações
modelo de transição (probabilidade de transição de estado)
modelo de recompensas

recompensas (infinitas ou recompensas descontadas no tempo (perda de oportunidade - gama(0, 1)))

politica é uma função que dado o estado indica a ação a ser tomada (deterministica), não deterministica (probabilistica) dá a probabilidade de escolher uma ação

recompensa que ganha a fazer uma determinada ação + soma(gama * utilidade do estado seguinte)

politica ótima: maximiza a utilidade esperada

No calculo da utilidade é usada programação iterativa em vez de recursiva, para guardar soluções intermédiasn(em memória em vez de usar o stack)

A politica converge mais cedo que a utilidade, por isso o delta max é usado para verificar a convergência da politica (rever slide 19)

restrições sobre o problema que reduzem a complexidade e possibilidade de calcular a politica ótima (racionalidade limitada)

Como é que funciona um processo de decisão sequencial?
R: Agir e observar o mundo. 

Aprendizagem por reforço (interativa), o sistema vai vendo o que é certo e errado (tentando) e vai aprendendo com o tempo, e vai ajustando a politica, para maximizar a utilidade esperada.

prompt injection: a vulnerability that affects some AI/ML models, particularly certain types of language models. Prompt injection attacks aim to elicit an unintended response from LLM-based tools. One type of attack involves manipulating or injecting malicious content into prompts to exploit the system. (see about this)

Resultado:
Qual é o estado para qual o sistema converge?
Qual é a recompensa que o sistema vai ter?

A memmória é o grau mais básico da inteligência. Mas aprender não é memorizar é ganhar capacidade de adaptação.

3 elementos importantes na aprendizagem (IA restrita)
- qual é a tarefa a ser aprendida (T)
- métrica de desempenho (D)
- com base na experiência, como é que o sistema vai aprender (E)

Na IA geral, o sistema é capaz de ter um desempenho signficativo em qualquer tarefa, sem ter sido programado para isso (conhecimento alargado do mundo). Nível de abrangência do conhecimento do mundo.

Métrica implicita nas associações estimulo-resposta (aprendizagem por associação)

Apredizagem por Reforço:


Aprendizagem de Valor de Ação:

Qn(a) = Qn-1(a) + 1*n (Ran - Qn-1(a))
, onde Ran - Qn-1(a) é o erro de previsão e só funciona para distribuições estacionárias (a recompensa é constante, não varia ao longo do tempo)

Distribuição não estacionária (a recompensa não é constante, varia ao longo do tempo)

Fator alfa (0, 1) - taxa de aprendizagem (0, 1), que é o fator de ajuste da aprendizagem, que é aplicado ao erro de previsão, para ajustar a previsão, de forma exponencial, por cada unidade de tempo que passa. Regula o efeito das amostras passadas e presentes.

Se alfa = 0, o sistema não aprende com o sistema, porque o erro de previsão é anulado. Se alfa = 1, o sistema aprende com o sistema, porque o erro de previsão é maximizado (torna-se um agente reactivo, é guiado pela recompensa imediata)

Compromisso Explorar/Aproveitar (trade-off)
Explorar: para obter conhecimento
Aproveitar: o conhecimento adquirido para maximizar a recompensa

Greedy vs E-Greedy

Epsilon (0, 1) - fator de exploração, que é o fator de ajuste da exploração, que é aplicado à taxa de aprendizagem, para ajustar a exploração, de forma exponencial, por cada unidade de tempo que passa. Regula o efeito das amostras passadas e presentes.
Se o sistema já tem a experiência total então o Epsilon é zero, porque o sistema já tem a experiência total. Se o sistema não tem a experiência total então o Epsilon é um, porque o sistema não tem a experiência total.

E de acordo com métricas que o sistema consulta para ter ideia de quanto já aprendeu em relação ao que pode ser aprendido, o sistema ajusta o Epsilon, para explorar ou aproveitar o conhecimento adquirido.

Aprender a propria politica:
Dado um estado o valor de fazer uma determinada ação é esta.      

Aprendizagem Por Reforço: Q(s,a) = R(s,a) + gama * max(Q(s',a'))

Algoritmo SARSA (State-Action-Reward-State-Action):
- o sistema vai tentar resolver o problema em tentativas (episódios),
- cria uma estimativa interna do valor de cada ação em cada estado.
