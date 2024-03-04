package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.Comando;

/**
 * Encapsula uma ação gerada pelos atuadores do Agente.
 */
public class Accao {

    /**
     * Caracteriza uma ação.
     */
    private Comando comando;

    /**
     * Permite consultar o valor atual do Comando correspondente a esta Ação, que é uma variável mutável, mas apenas acessível em modo leitura.
     */
    public Comando getComando() {
        return comando;
    }

    public Accao(Comando comando) {
        this.comando = comando;
    }
}