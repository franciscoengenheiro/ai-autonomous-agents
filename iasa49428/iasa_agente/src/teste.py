# Módulo para testar todos os agentes

from sae import Simulador
# Comment all lines except the one you want to test
from agente.agente_reactivo import AgenteReactivo as Agente

# Executar simulador de SAE
# param 1: index of the chosen simulation
# param 2: agente
Simulador(1, Agente()).executar()