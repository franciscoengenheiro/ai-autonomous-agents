package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Ambiente;
import iasa_jogo.src.ambiente.Comando;
import iasa_jogo.src.ambiente.Evento;

import java.util.Map;
import java.util.Scanner;

/**
 * Caracteriza um ambiente que é específico de um determinado jogo.
 */
public class AmbienteJogo implements Ambiente {

    /**
     * Representa o evento atual intrínseco a este ambiente.
     */
    private EventoJogo evento;

    /**
     * Detem o mapeamento entre os comandos que podem ser introduzidos pelo utilizador e os eventos que representam.
     * Foi utilizada a programação declarativa para declarar, passando a redundância, esse mapeamento que não é mutável.
     */
    private final Map<String, EventoJogo> eventos = Map.of(
            "s", EventoJogo.SILENCIO,
            "r", EventoJogo.RUIDO,
            "a", EventoJogo.ANIMAL,
            "f", EventoJogo.FUGA,
            "o", EventoJogo.FOTOGRAFAR,
            "t", EventoJogo.TERMINAR
    );

    public Map<String, EventoJogo> getEventos() {
        return eventos;
    }

    private final Scanner scanner = new Scanner(System.in);

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

    /**
     * Gerar um evento significa pedir ao utilizador que introduza um comando, em formato de texto, ler esse texto e,
     * segundo o mapeamento de comandos para eventos, devolver o evento correspondente.
     */
    private EventoJogo gerarEvento() {
        System.out.println("\nEvento? ");
        String textoComando = scanner.next();
        return eventos.get(textoComando);
    }

    /**
     * Devolve o evento atual intrínseco a este ambiente.
     */
    public EventoJogo getEvento() {
        return evento;
    }
}
