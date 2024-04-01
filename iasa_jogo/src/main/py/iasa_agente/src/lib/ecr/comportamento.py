from abc import ABC, abstractmethod
    
class Comportamento(ABC):

    """
    Define o módulo comportamental associado a um agente reativo. Encapsula um conjunto de reações relacionadas entre si, possivelmente com uma sequência temporal, de forma a atingir um ou ou mais objetivos. Associado a um objetivo podem existir sub-objetivos.

    Tipos de Comportamento:
    - Comportamento Fixo (Resposta Fixa, gera uma ação em permanência);
    - Comportamento Simples (Reação);
    - Comportamento Composto (agrega sub-comportamentos, ao qual está associado um mecanismo de seleção de ação de forma a determinar a acção a realizar em função das respostas dos mesmos)
    """
    
    @abstractmethod
    def activar(self, percepcao):
        """
        TODO
        """