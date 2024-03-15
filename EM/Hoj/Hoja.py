
from EM.ElementoMapa import ElementoMapa


class Hoja(ElementoMapa):
    def __init__(self, em):
        self.em = em
    
    def recorrer(self, unBloque):
        unBloque.value(self)

    #No hacer caso a este metodo
    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        pass  
    
    def recorrer(self):
        pass
