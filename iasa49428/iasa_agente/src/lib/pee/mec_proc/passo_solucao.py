from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    
    """
    Contentor de informação que representa um passo de uma solução. Cada passo é composto pelo estado do nó antecessor e pelo operador usado para gerar o nó atual.
    """
    estado: Estado
    operador: Operador