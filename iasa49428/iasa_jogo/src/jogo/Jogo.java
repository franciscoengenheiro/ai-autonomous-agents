package iasa_jogo.src.jogo;

import iasa_jogo.src.jogo.ambiente.AmbienteJogo;
import iasa_jogo.src.jogo.ambiente.EventoJogo;
import iasa_jogo.src.jogo.personagem.Personagem;

/**
 * Representa um jogo que é composto por um ambiente e uma personagem específicos do mesmo.
 */
public class Jogo {

    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    /**
     * Entry point do programa, responsável por criar o ambiente e a personagem, e executar o ciclo do jogo.
      */
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Executa o jogo em ciclo até que o evento seja recebido seja um pedido para terminar o jogo.
     * Em cada iteração do ciclo, o ambiente é evoluido, ou seja, é gerado um novo evento, e a personagem executa a sua acção.
     * Este método é privado porque depende da implementação de um ambiente e de uma personagem, e não deve ser executado no exterior.
     */
    private static void executar() {
        ambiente.getEventos().forEach((k, v) -> System.out.println(k + " - " + v));
        do  {
            // É utilizado o *do-while* em vez do *while* porque o ambiente deve ser evoluído
            // pelo menos uma vez para que o evento associado seja populado pela primeira vez,
            // senão temos NullPointerException (NPE)
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}
