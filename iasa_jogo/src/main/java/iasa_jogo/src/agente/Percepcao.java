package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.Evento;

/**
 * Encapsula um evento percecionado pelos sensores do Agente.
 */
public class Percepcao {

    /**
     * Caracteriza uma percepção.
     */
    private Evento evento;

    /**
     * Permite consultar o valor atual do Evento percecionado, que é uma variável mutável, mas apenas acessível em modo leitura.
     */
    public Evento getEvento() {
        return evento;
    }

    public Percepcao(Evento evento) {
        this.evento = evento;
    }
}
