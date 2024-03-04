package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Evento;

public enum EventoJogo implements Evento {
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFAR, TERMINAR;

    @Override
    public void mostrar() {
        System.out.printf("Evento: %s\n", this);
    }
}
