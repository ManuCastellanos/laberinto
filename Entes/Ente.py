from abc import ABC, abstractmethod

class Ente(ABC):
    
    def __init__(self):
        self.modo = None    
        self.vidas = 0
        self.poder = 0
        self.posicion = None
        self.juego= None
    
    def esPersonaje(self):
        return False
    
    def esBicho(self): 
        return False
    
    def actua(self):
        self.modo.actua(self)
        
    def irA(self, unaOr):
        unaOr.caminar(self)
        
    def irAlNorte(self):
        self.posicion.irAlNorte(self)
    
    def irAlSur(self):
        self.posicion.irAlSur(self)
    
    def irAlEste(self):
        self.posicion.irAlEste(self)
    
    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    