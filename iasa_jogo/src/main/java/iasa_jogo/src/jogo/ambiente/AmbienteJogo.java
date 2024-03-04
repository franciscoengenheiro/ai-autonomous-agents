package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Ambiente;
import iasa_jogo.src.ambiente.Comando;
import iasa_jogo.src.ambiente.Evento;

import java.util.Map;
import java.util.Scanner;

public class AmbienteJogo implements Ambiente {

    private EventoJogo evento;

    // Programação Declarativa
    private final Map<String, EventoJogo> eventos = Map.of(
            "s", EventoJogo.SILENCIO,
            "r", EventoJogo.RUIDO,
            "a", EventoJogo.ANIMAL,
            "f", EventoJogo.FUGA,
            "o", EventoJogo.FOTOGRAFAR,
            "t", EventoJogo.TERMINAR
    );

    private Scanner scanner = new Scanner(System.in);

    public AmbienteJogo() {

    }

    public Map<String, EventoJogo> getEventos() {
        return eventos;
    }


    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

    @Override
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    private EventoJogo gerarEvento() {
        System.out.println("\nEvento? ");
        String textoComando = scanner.next();
        return eventos.get(textoComando);
    }

    public EventoJogo getEvento() {
        return evento;
    }
}
