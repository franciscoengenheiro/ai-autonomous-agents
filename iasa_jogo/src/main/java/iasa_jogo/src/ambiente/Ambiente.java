package iasa_jogo.src.ambiente;

/**
 * Define um espaço onde se pode observar o estado do mundo e
 * executar comandos.
 * TODO: Explicar os métodos após utilização.
 */
public interface Ambiente {
    void evoluir();
    Evento observar();
    void executar(Comando comando);
}
