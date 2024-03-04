package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.Ambiente;
import iasa_jogo.src.ambiente.Comando;
import iasa_jogo.src.ambiente.Evento;

/**
 * Representa um sistema computacional inteligente responsável por percecionar/captar eventos,
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
    Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    void executar() {
        // TODO(use control?)
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
