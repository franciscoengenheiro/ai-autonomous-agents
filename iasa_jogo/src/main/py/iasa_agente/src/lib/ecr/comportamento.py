from abc import ABC, abstractmethod
    
class Comportamento(ABC):

    """
    Define o módulo comportamental associado a um agento reativo. Encapsula um conjunto de reações relacionadas entre si, possivelmente com uma sequência temporal, de forma a atingir um objetivo.

    Tipos de Comportamento:
    - Comportamento Fixo (Resposta Fixa), gera uma ação em permanência
    - Comportamento Simples (Reação)
    - Comportamento Composto (agrega outros comportamentos, ao qual está associado um mecanismo de seleção de ação - para determinar a acção a realizar em função das respostas dos mesmos)
    """

    @abstractmethod
    def activar(self, percepcao):
        """
        TODO
        """