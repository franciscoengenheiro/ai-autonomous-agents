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