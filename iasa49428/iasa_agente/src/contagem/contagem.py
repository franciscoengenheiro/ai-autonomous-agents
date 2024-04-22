from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade


VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2] # Problema encontrado com operador -1, a procura é infinita porque existem possíveis ciclos [-1, 1, 2, -1, 1, 2, -1, ... ]

PROBLEMA = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

mec_proc = ProcuraProfLim(45)

solucao = mec_proc.procurar(PROBLEMA)

# Mostrar a solução
if solucao:
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)
        