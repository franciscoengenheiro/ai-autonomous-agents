package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.ambiente.Evento;
import java.util.HashMap;
import java.util.Map;

/**
 * Representa uma série de transições possíveis a partir de um determinado momento no tempo.
 * Responsável por processar eventos e gerar transições para um estado sucessor, ao qual pode ou não estar associada uma ação.
 */
public class Estado {
    private final String nome;

    /**
     * Representa todas as transições possíveis a partir deste estado.
     * É a partir deste suporte que são implementadas as funções de transição de estado e de saída, delta e lambda, respetivamente.
     */
    private final Map<Evento, Transicao> transicoes;

    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<>();
    }

    public String getNome() {
        return nome;
    }

    /**
     * Acede à tabela de transicoes e verifica se existe uma transicao para o evento recebido
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Neste método foi delegada a sua responsabilidade para o método (overload) de forma a que não exista redundância de código.
     * @see #transicao(Evento, Estado, Accao)
     */
    public Estado transicao(Evento evento,
                            Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Cria uma nova transição com o estado sucessor recebido e a ação a executar, se esta existir.
     * Adiciona a transição criada à tabela de transições, associada ao evento recebido.
     */
    public Estado transicao(Evento evento,
                            Estado estadoSucessor,
                            Accao acao) {
        Transicao transicao = new Transicao(estadoSucessor, acao);
        transicoes.put(evento, transicao);
        // Permite fazer múltiplas chamadas encadeadas: fluent interface
        return this;
    }
}


