from typing import override

from pdm.modelo.modelo_pdm import ModeloPDM


class ModProbPdm(ModeloPDM):
    
    """
    Representa um modelo de um Processo de Decisão de Markov (PDM) determinístico.

    Descrição do problema:
    [1 (et), 2, 3, 4, 5, 6, 7 (et)] , onde "et" é um estado terminal.

    Acções possíveis:
    - '<' (move to the left)
    - '>' (move to the right)

    Recompensas:
    - estado 1: -1
    - estado 7: 1
    """

    @override
    def S(self):
        return [1, 2, 3, 4, 5, 6, 7]

    @override
    def A(self, s):
        # Edit: added no actions for terminal states
        return ["<", ">"] if s not in [1, 7] else []

    @override
    def T(self, s, a, sn):
        # estados terminais
        if s == 1 or s == 7:
            return 0.0
        else:
            return 1.0  # estados não terminais e porque o ambiente é determinístico

    @override
    def R(self, s, a, sn):
        if s == 2 and a == "<" and sn == 1:  # R(2, '<', 1)
            return -1.0
        elif s == 6 and a == ">" and sn == 7:  # R(6, '>', 7)
            return 1.0
        else:
            return 0.0

    @override
    def suc(self, s, a):
        # Edit: a better way: [max(1, s-1) if a == '<' else min(7, s+1)]
        if s == 1 and a == "<" or s == 7 and a == ">":
            return [s]
        elif a == "<":
            return [s - 1]
        else:
            return [s + 1]
