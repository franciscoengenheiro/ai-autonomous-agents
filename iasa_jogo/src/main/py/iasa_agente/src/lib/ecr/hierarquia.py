from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):

    """
    Representa uma forma de comportamento composto com um mecanismo de seleção de ação de prioridade por hierarquia fixa de subsunção (supressão e substituição). Os comportamentos mais altos na hierarquia têm prioridade sobre os mais baixos (correção de acção), e não variam consoante o tempo. (e.g., o comportamento "carregar bateria", tem sempre prioridade sobre "explorar" ou "evitar obstáculo, pois representa um comportamento mais básico e fundamental para a sobrevivência do agente)
    """

    def seleccionar_accao(accoes):
        """
        Considera-se que no paramêtro "accoes" a lista de acções vem ordenada consoante a prioridade das acoes associadas aos comportamentos que compõem o comportamento composto. Dessa forma, a acção de maior prioridade é a primeira acção da lista de acções, que é retornada. Poderá não ser retornada nenhuma acção caso a lista de acções esteja vazia.
        """
        if accoes:
            return accoes[0]