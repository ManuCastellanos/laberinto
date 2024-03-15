from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None
        
    #Getters y Setters de la clase
    def get_padre(self):
        return self.padre

    def set_padre(self, anObject):
        self.padre = anObject

    def esBomba(self):
        return False

    def esHabitacion(self):
        return False

    def esPared(self):
        return False

    def esPuerta(self):
        return False

    #Patrón: Iterator
    @abstractmethod
    def recorrer(self, unBloque):
        raise NotImplementedError("La subclase debe implementar el metodo recorrer()")
    

    @abstractmethod
    def entrar(self):
        raise NotImplementedError("La subclase debe implementar el metodo entrar()")

    @abstractmethod
    def entrar_alguien(self, alguien):
        raise NotImplementedError("La subclase debe implementar el metodo entrar_alguien()")


