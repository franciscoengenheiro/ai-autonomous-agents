package iasa_jogo.src.agente;

/**
 * Representa o módulo de processamento interno do Agente, que pode ser equiparado ao seu cerébro, e que é responsável por processar eventos/sensores, e a partir destes, gerar ações.
 */
@FunctionalInterface
public interface Controlo {

    /**
     * Processa a perceção do agente e devolve a ação a ser executada, como resposta.
     */
    Accao processar(Percepcao percepcao);
}
