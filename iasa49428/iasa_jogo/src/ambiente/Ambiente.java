package iasa_jogo.src.ambiente;

/**
 * Define um espaço, real ou virtual, onde se pode observar o estado do mundo e
 * executar comandos.
 */
public interface Ambiente {

    /**
     * Evoluir o ambiente significa atualizar o evento atual com um novo evento gerado no momento.
     */
    void evoluir();

    /**
     * Observar o ambiente significa consultar o evento atual, mostrando-o ao exterior e devolvendo-o.
     */
    Evento observar();

    /**
     * Executar um comando significa mostrar o comando.
     */
    void executar(Comando comando);
}
