# from pee.larg.procura_largura import ProcuraLargura as MecanismoProcura
# from pee.melhor_prim.procura_aa import ProcuraAA as MecanismoProcura
# from pee.melhor_prim.procura_sofrega import ProcuraSofrega as MecanismoProcura
# from pee.prof.procura_prof_lim import ProcuraProfLim as MecanismoProcura
# from pee.prof.procura_profundidade import ProcuraProfundidade as MecanismoProcura
# from pee.prof.procura_prof_iter import ProcuraProfIter as MecanismoProcura
from deposito.modelo.problema_deposito import ProblemaDeposito
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif as MecanismoProcura

VALOR_INICIAL = 0
VALOR_FINAL = 9

mec_proc = MecanismoProcura()
PROBLEMA = ProblemaDeposito(VALOR_INICIAL, VALOR_FINAL)

# print(mec_proc.__class__.__name__)
solucao = mec_proc.procurar(PROBLEMA)

# Mostrar a solução
if solucao:
    for passo in solucao:
        # Encher[2], Encher[2], Vazar[2], Vazar[3]
        print(passo.operador.__class__.__name__, passo.operador._volume, end=", ")
            