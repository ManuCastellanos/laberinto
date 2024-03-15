from EM.ElementoMapa import ElementoMapa
from EM.ElementoMapa import ElementoMapa


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    #Getter y Setter de la clase
    def get_lado1(self):
        return self.lado1
    
    def set_lado1(self, anObject):
        self.lado1 = anObject
    
    def get_lado2(self):
        return self.lado2
    
    def set_lado2(self, anObject):
        self.lado2 = anObject
    
    def get_abierta(self):
        return self.abierta
    
    def set_abierta(self, anObject):
        self.abierta = anObject
    
    def __str__(self):
        return "Puerta de hab" + str(self.lado1.num) + " a hab" + str(self.lado2.num)

    def __repr__(self, aStream):
        aStream.nextPutAll('Pt-')
        aStream.nextPutAll(str(self.lado1.num))
        aStream.nextPutAll('-')
        aStream.nextPutAll(str(self.lado2.num))
        
    #testing
    def esPuerta (self):
        return True
    
    
    #No hacer caso a este metodo
    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        pass  
    
    def recorrer(self):
        pass
