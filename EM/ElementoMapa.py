class ElementoMapa():
    def __init__(self):
        self.padre = None
        
    def es_padre(self, anObject):
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
    def recorrer(self, unBloque):
       unBloque(self)

    def entrar(self):
        pass
    def entrar_alguien(self, alguien):
        pass

