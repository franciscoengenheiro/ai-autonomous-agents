package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.Ambiente;
import iasa_jogo.src.ambiente.Comando;
import iasa_jogo.src.ambiente.Evento;

/*
Implementação -> Arquitetura -> Modelo -> (volta para) Implementação

Implementação pode ser estrutural ou comportamental:
UML -> Estrutura: define a estrutura de um sistema, ou seja, a forma como os componentes se relacionam entre si;
Sequence Diagram -> Comportamento: mostra a interação entre objetos, ou seja, a forma como os componentes comunicam entre si.

Diagramas de Atividade:
- Representam o fluxo de controlo de um sistema, ou seja, a sequência de atividades que um sistema executa;
- Compostos por:
    - Nós (nó inicial, nó final, nó de decisão, nó de fusão, nó de bifurcação, nó de junção, nó de atividade);
    - Guardas (condições de transição);
    - Partições (divisão do fluxo de controlo, que são as atividades realizadas por uma parte específica do modelo)

Acoplamento (inter-modular):
- Unidirecional vs Bidirecional (uni representa menos acoplamento);
- Visibilidade (menos visibilidade representa menos acoplamento);
- (ordem de menos acoplamento para mais):
Herança -> Composição -> Agregação -> Associação -> Dependência

Coesão (intra-modular):
- Os módulos que constituem o software estão organizados por conteúdo;
- Cada módulo deve ter uma única responsabilidade (Single Responsibility Principle)

Inteligência => (implica) Autonomia
- vice-versa não é verdadeiro

Principios de Arquitetura:
- Abstração;
- Modularização;
- Factorização;
  - Herança (estrutural);
  - Delegação (funcional)
*/

/**
 * Representa um sistema computacional inteligente autónomo responsável por percecionar/captar eventos,
 * provenientes do ambiente, atráves de sensosres, processá-los e gerar ações como resposta, atráves de atuadores.
 */
public class Agente {

    private final Controlo controlo;
    private final Ambiente ambiente;

    /**
     * Este construtor tenta definir as seguintes relações:
     * - Agente o---- Controlo, ou seja o Agente só existe se estiver associado ao módulo Controlo (relação de Composição);
     * - Agente ----> Ambiente, ou seja o Agente conhece o Ambiente, mas o Ambiente não conhece o Agente (relação unidireccional).
     * Adicionalmente, ambos os parametros representam interfaces, colocando o Agente numa posição de independência em relação
     * à respetiva implementação destes (injeção de dependências).
     */
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * O Agente executa o seu ciclo de vida, delegando, ao módulo de Controlo, o processamento da perceção e a geração da ação resultante.
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        atuar(accao);
    }

    /**
     * O Agente ao observar o Ambiente perceciona/capta um evento e envia essa informação para o módulo de Controlo para ser processado.
     */
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /**
     * Define o comportamento de um atuador do Agente, que, ao receber uma ação válida, é consultado o valor do comando atual que lhe está associado, de forma a que o Ambiente o possa executar.
     */
    protected void atuar(Accao accao) {
        if (accao != null) {
            Comando comando = accao.getComando();
            ambiente.executar(comando);
        }
    }
}
