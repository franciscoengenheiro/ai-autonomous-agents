from ecr.comport_comp import ComportComp


class Prioridade(ComportComp):

    """
    Representa uma forma de comportamento composto com um mecanismo de seleção de ação de prioridade dinâmica, e que portanto a prioridade dos comportamentos associados varia consoante o tempo. Os comportamentos mais altos na hierarquia têm prioridade sobre os mais baixos (correção de acção), e não variam consoante o tempo. (e.g., o comportamento "evitar obstáculo" tem prioridade sobre "explorar" quando o agente se encontra próximo de um obstáculo, mas "explorar" tem prioridade sobre "evitar obstáculo" quando não existem obstáculos próximos)        
    """

    def seleccionar_accao(accoes):

        """
        Retorna a primeira acção da lista de acções, que é a acção de maior prioridade, iterando a lista de acções e guardando referência para a acção de maior prioridade. Mesmo que existam várias acções com a mesma prioridade, a primeira acção desse conjunto é retornada. Poderá não ser retornada nenhuma acção caso a lista de acções esteja vazia.
        """
        if accoes: 
            funcao_prioridade = lambda it: it.prioridade # função transformadora
            return max(accoes, key=funcao_prioridade)
        


        
    