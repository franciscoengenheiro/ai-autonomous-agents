package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Ambiente;
import iasa_jogo.src.ambiente.Comando;
import iasa_jogo.src.ambiente.Evento;

import java.util.Map;

public class AmbienteJogo implements Ambiente {

    private static final Map<String, EventoJogo> eventos = Map.of(
            "s", EventoJogo.SILENCIO,
            "r", EventoJogo.RUIDO,
            "a", EventoJogo.ANIMAL,
            "f", EventoJogo.FUGA,
            "o", EventoJogo.FOTOGRAFAR,
            "t", EventoJogo.TERMINAR
    );

    public AmbienteJogo() {

    }

    public Map<String, EventoJogo> getEventos() {
        return eventos;
    }


    @Override
    public void evoluir() {

    }

    @Override
    public Evento observar() {
        return null;
    }

    @Override
    public void executar(Comando comando) {

    }

    private EventoJogo gerarEvento() {

    }
}
