from abc import ABC, abstractmethod

class Estado(ABC):
    """
    Representação única e simbolica de um conjunto de informações concretas que caracterizam um estado da modelação de um problema. No âmbito do raciocínio automático, os estados abstraem os aspetos (configurações) estruturais que caracterizam o problema. Ao conjunto de estados possíveis de um problema e às transições entre eles, dá-se o nome de espaço de estados.
    """

    def __hash__(self):
        return self.id_valor()

    def __eq__(self, other):
        """
        Dois estados são iguais se tiverem o mesmo valor de identificação e forem da mesma classe.
        """

        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()

    @abstractmethod
    def id_valor(self):
        """
        Permite abstrair a forma como o valor de identificação do estado é obtido, de forma a que esteja dependente da implementação do estado concreto.
        """
