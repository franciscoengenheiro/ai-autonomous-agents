# Module to test the agents

from sae import Simulador
# Comment all lines except the one you want to test
# from agente.agente_reactivo import AgenteReactivo as Agente
from agente.agente_delib_pee import AgenteDeiberativoPee as Agente

# Execute simulation:
# param 1: index of the chosen ambient configuration
# param 2: agent to be tested
Simulador(4, Agente()).executar()
