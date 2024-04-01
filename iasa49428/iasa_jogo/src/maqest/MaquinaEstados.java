package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.ambiente.Evento;

/**
 * Modulação do comportamento associado a um sistema computacional que permite a representação de um sistema de estados finitos.
 * É composto por:
 * - Um conjunto finito de estados - Q;
 * - Um conjunto finito de eventos - E;
 * - Um conjunto finito de ações - Z;
 * - Uma função de transição de estado - sigma: Q x E -> Q;
 * - Uma função de saída - lambda: Q x E -> Z;
 * Tipos de Máquinas de Estados:
 * - Máquina de Moore -> onde a saída depende somente do estado atual;
 * - Máquina de Mealy -> onde a saída depende da entrada e do estado atual
 */
public class MaquinaEstados {
    private Estado estado;

    /**
     * Cria uma máquina de estados com um estado inicial.
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Obtem uma transição, processando o evento atual.
     * Se a transição for válida, atualiza o estado atual e retorna a ação associada.
     * Onde:
     * - o Evento é o alfabeto de entrada E (conjunto de eventos)
     * - A Ação é o alfabeto de saída Z (conjunto de ações)
     * Que são processados, respetivamente pela:
     * - Função de transição de estado sigma: Q x E -> Q, onde Q é o conjunto de estados
     * - Função de saída lambda: Q x E -> Z
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.estadoSucessor();
            return transicao.acao();
        } else {
            return null;
        }
    }

    public Estado getEstado() {
        return estado;
    }
}
