package iasa_jogo.src.jogo.personagem;

import iasa_jogo.src.agente.Agente;
import iasa_jogo.src.jogo.ambiente.AmbienteJogo;

/**
 * Representa uma personagem do jogo, que é um Agente com um módulo Controlo e Ambiente específicos.
 */
public class Personagem extends Agente {

    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}
