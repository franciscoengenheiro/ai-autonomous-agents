package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;

/**
 * Contentor de informação que representa a transição entre dois estados de uma máquina de estados.
 * Armazena o estado sucessor e a ação a executar associada à transição de um estado.
 *
 * @see MaquinaEstados
 * @see Estado
 * @see Accao
 */
public class Transicao {
    private final Estado estadoSucessor;
    private final Accao accao;

    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    public Estado estadoSucessor() {
        return estadoSucessor;
    }

    public Accao acao() {
        return accao;
    }
}
