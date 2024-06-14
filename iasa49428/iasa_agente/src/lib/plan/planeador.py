from abc import ABC, abstractmethod

class Planeador(ABC):

    """
    No contexto de um controlo deliberativo, corresponde a um componente que exerce raciocínio automático, mais concretamente, prático (orientado para a ação - interação permanente com o mundo, ao qual está associado o processo de tomada de decisão), e que produz, através do modelo do mundo, o plano de ação que o agente deve executar para atingir os objetivos provenientes do módulo de deliberação.
    """
    
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """
        Tendo em conta um modelo do plano e um conjunto de objectivos, devolve um plano, constituído por uma sequência de acções, que permite atingir esses objectivos.
        """
    