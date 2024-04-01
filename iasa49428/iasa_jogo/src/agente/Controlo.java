package iasa_jogo.src.agente;

/**
 * Representa o módulo de processamento interno do Agente, que pode ser equiparado ao seu cerébro, e que é responsável por processar eventos, e a partir destes, gerar ações condicionadas ou não por um módulo de deliberação, dependedo do tipo de modelo.
 * Modelos:
 * - Reativo: Associações diretas entre perceções e ações, tipo estímulo-resposta.
 * - Deliberativo: Processamento de eventos e geração de ações condicionadas por um módulo de deliberação (raciocínio e tomada de decisão).
 * - Híbrido: Combinação de ambos os modelos.
 */
@FunctionalInterface
public interface Controlo {

    /**
     * Processa a perceção que o Agente obteve através dos seus sensores e devolve a ação a ser executada, como resposta, a partir da perceção.
     * Dependendo do modelo de controlo, a ação pode ser gerada diretamente a partir da perceção, ou condicionada por um módulo de deliberação que está intrínseco ao Controlo.
     */
    Accao processar(Percepcao percepcao);
}
