package iasa_jogo.src.jogo.personagem;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.agente.Agente;
import iasa_jogo.src.agente.Controlo;
import iasa_jogo.src.agente.Percepcao;
import iasa_jogo.src.ambiente.Evento;
import iasa_jogo.src.jogo.ambiente.ComandoJogo;
import iasa_jogo.src.jogo.ambiente.EventoJogo;
import iasa_jogo.src.maqest.Estado;
import iasa_jogo.src.maqest.MaquinaEstados;

/**
 * Representa o módulo controlo do Agente Personagem, que utiliza uma máquina de estados do tipo Mealy.
 *
 * @see MaquinaEstados
 * @see Controlo
 * @see Agente
 * @see Personagem
 */
public class ControloPersonagem implements Controlo {

    private final MaquinaEstados maquinaEstados;

    /**
     * Define a máquina de estados do controlo da personagem.
     * - Estados possíveis;
     * - Definição de possíveis acções;
     * - Transições entre estados
     */
    public ControloPersonagem() {
        // Definição dos estados, que representam o conjunto de estados Q
        Estado procura = new Estado("Procura");
        Estado observacao = new Estado("Observacao");
        Estado inspecao = new Estado("Inspecao");
        Estado registo = new Estado("Registo");

        // Definição de Ações, que representam o alfabeto de saída Z (conjunto de ações)
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

        // Definição das transições que engloba:
        // (função da transição de estado(&), &: Q x E -> Q, onde Q é o
        // conjunto de estados e E é o conjunto de eventos)
        // Procura:
        procura
                .transicao(EventoJogo.SILENCIO, procura, procurar)
                .transicao(EventoJogo.RUIDO, inspecao, aproximar);

        // Observação:
        observacao
                .transicao(EventoJogo.FUGA, inspecao)
                .transicao(EventoJogo.ANIMAL, registo, observar);

        // Registo:
        registo
                .transicao(EventoJogo.ANIMAL, registo, fotografar)
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura);

        // Inspeção:
        inspecao
                .transicao(EventoJogo.RUIDO, inspecao, procurar)
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar);

        // Inicia a máquina de estados com um estado inicial
        maquinaEstados = new MaquinaEstados(procura);
    }


    public Estado getEstado() {
        return maquinaEstados.getEstado();
    }

    @Override
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao acao = maquinaEstados.processar(evento);
        mostrar();
        return acao;
    }

    /**
     * Mostra o estado atual.
     */
    private void mostrar() {
        System.out.printf("\nEstado: %s\n", getEstado().getNome());
    }

}
