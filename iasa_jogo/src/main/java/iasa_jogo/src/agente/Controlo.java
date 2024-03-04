package iasa_jogo.src.agente;

/**
 * Representa o módulo principal do Agente, que pode ser equiparado ao seu cerébro, e que é responsável por processar eventos/sensores, e a partir destes, gerar ações.
 */
@FunctionalInterface
public interface Controlo {
    Accao processar(Percepcao percepcao);
}
