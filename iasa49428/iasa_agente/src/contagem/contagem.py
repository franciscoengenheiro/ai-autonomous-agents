from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem as ProblemaContagem
# from pee.larg.procura_largura import ProcuraLargura as MecanismoProcura
# from pee.melhor_prim.procura_aa import ProcuraAA as MecanismoProcura
from pee.melhor_prim.procura_sofrega import ProcuraSofrega as MecanismoProcura
# from pee.prof.procura_prof_lim import ProcuraProfLim as MecanismoProcura
# from pee.prof.procura_profundidade import ProcuraProfundidade as MecanismoProcura
# from pee.prof.procura_prof_iter import ProcuraProfIter as MecanismoProcura
# from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif as MecanismoProcura

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2] # Problema encontrado com operador -1, a procura é infinita porque existem possíveis ciclos [-1, 1, 2, -1, 1, 2, -1, ... ]

PROBLEMA = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

HEURISTICA = HeuristicaContagem(VALOR_FINAL)

# mechanism name
# print the solution as an array
# print solution dimension
# print the solution cost
# print the number of nodes processed
# print the maximum number of nodes in memory

mec_proc = MecanismoProcura()
# print(mec_proc.__class__.__name__)
solucao = mec_proc.procurar(PROBLEMA, HEURISTICA)

# Mostrar a solução
if solucao:
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)
            