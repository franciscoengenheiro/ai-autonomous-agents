package iasa_jogo.src.ambiente;

/**
 * Define algo que pode ser observado.
 */
@FunctionalInterface
public interface Observavel {
    /**
     * Mostra o observável ao exterior.
     */
    void mostrar();
}
