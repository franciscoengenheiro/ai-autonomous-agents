from lib.pdm.pdm import PDM
from exercicio.mod_pdm.mod_prob_pdm import ModProbPdm

modelo = ModProbPdm()
gama = 0.5
delta_max = 0.0
pdm = PDM(modelo, gama, delta_max)

U, P = pdm.resolver()
print(U)
print(P)

# Example:
# U = {1: 0, 2: 0.5, 3: 0.8, 4: 0.3, etc...}
# P = {2: '>', 3: '>', 4: '>', etc...}
