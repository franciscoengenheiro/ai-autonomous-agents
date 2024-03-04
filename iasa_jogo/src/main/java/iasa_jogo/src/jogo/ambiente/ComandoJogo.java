package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Comando;

/**
 * Representa os comandos que podem ser executados durante o jogo.
 */
public enum ComandoJogo implements Comando {
    PROCURAR, APROXIMAR, OBSERVAR, FOTOGRAFAR;

    @Override
    public void mostrar() {
        System.out.printf("Acção: %s\n", this);
    }

}
