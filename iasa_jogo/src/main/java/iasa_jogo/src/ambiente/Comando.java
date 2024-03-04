package iasa_jogo.src.ambiente;

/**
 * Caracteriza um comando que pode ser executado no Ambiente.
 */
@FunctionalInterface
public interface Comando {
    void mostrar();
}
