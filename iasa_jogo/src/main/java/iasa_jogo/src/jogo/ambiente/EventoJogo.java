package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Comando;

public enum EventoJogo implements Comando {
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFAR, TERMINAR;

    @Override
    public void mostrar() {

    }
}
