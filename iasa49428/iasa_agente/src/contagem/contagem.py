from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem as ProblemaContagem

from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2] # Problema encontrado com operador -1, a procura é infinita porque existem possíveis ciclos [-1, 1, 2, -1, 1, 2, -1, ...]

PROBLEMA = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
HEURISTICA = HeuristicaContagem(VALOR_FINAL)

mecanismos_procura = [
    ProcuraProfundidade,
    ProcuraProfLim,
    ProcuraProfIter,
    ProcuraLargura,
    ProcuraCustoUnif,
    ProcuraSofrega,
    ProcuraAA,
]

for MecanismoProcura in mecanismos_procura:
    print(f"Mecanismo de Procura: {MecanismoProcura.__name__}")

    mec_proc = MecanismoProcura()
    if isinstance(mec_proc, ProcuraInformada):
        solucao = mec_proc.procurar(PROBLEMA, HEURISTICA)
    else:
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
