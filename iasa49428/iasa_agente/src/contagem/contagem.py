from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem as ProblemaContagem

from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2]  # Problema encontrado com operador -1, a procura é infinita porque existem possíveis ciclos [-1, 1, 2, -1, 1, 2, -1, ...]

PROBLEMA = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
HEURISTICA = HeuristicaContagem(VALOR_FINAL)

mecanismos_procuras = [
    ProcuraProfundidade,
    ProcuraProfLim,
    ProcuraProfIter,
    ProcuraLargura,
    ProcuraCustoUnif,
    ProcuraSofrega,
    ProcuraAA,
]

# mechanism name
# print the solution as an array
# print solution dimension
# print the solution cost
# print the number of nodes processed
# print the maximum number of nodes in memory

for MecanismoProcura in mecanismos_procuras:
    print(f"Mecanismo de Procura: {MecanismoProcura.__name__}")

    mec_proc = MecanismoProcura()
    try:
        solucao = mec_proc.procurar(PROBLEMA, HEURISTICA)
    except TypeError:
        solucao = mec_proc.procurar(PROBLEMA)

    # Mostrar a solução
    if solucao:
        solucao_operadores = [passo.operador.incremento for passo in solucao]
        print("Solução:         ", solucao_operadores)
        print("Dimensão:        ", solucao.dimensao)
        print("Custo:           ", int(solucao.custo))
        print("Nós processados: ", mec_proc.get_nos_processados())
        print("Máx. nós memória:", mec_proc.get_max_nos_em_memoria())
    else:
        print("Não foi encontrada uma solução.")
    print()
