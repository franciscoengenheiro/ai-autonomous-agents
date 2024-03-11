package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Evento;

/**
 * Representa os eventos que podem ocorrer durante o jogo.
 */
public enum EventoJogo implements Evento {
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFAR, TERMINAR;

    @Override
    public void mostrar() {
        System.out.printf("\nEvento: %s", this);
    }
}
