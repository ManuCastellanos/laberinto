from abc import ABC, abstractmethod

class Orientacion(ABC):
    @abstractmethod
    def caminar(self, unEnte):
        raise NotImplementedError("Subclass must implement this method")

    @abstractmethod
    def ponerElemento(self, unEM, unContenedor):
        raise NotImplementedError("Subclass must implement this method")

        