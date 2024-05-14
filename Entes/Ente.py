from abc import ABC, abstractmethod
from State.Vivo import Vivo

class Ente(ABC):
    
    def __init__(self):
        self.modo = None    
        self.vidas = 0
        self.poder = 0
        self.posicion = None
        self.juego= None
        self.estado= Vivo()

        
    def irA(self, unaOr):
        unaOr.caminar(self)
    
    def irAlNorte(self):
        self.irA(self.juego.fabricarNorte()) #Como tengo el Singleton, si existe el norte, me lo devuelve
    
    def irAlSur(self):
        self.irA(self.juego.fabricarSur())
    
    def irAlEste(self):
        self.irA(self.juego.fabricarEste())
    
    def irAlOeste(self):
        self.irA(self.juego.fabricarOeste())
    
    def esPersonaje(self):
        return False
    
    def esBicho(self): 
        return False

    def esAura(self):
        return False
    
    def esBlitz(self):
        return False
    
    def actua(self):
        self.modo.actua(self)
   
    def atacar(self):
        ente = self.buscarEnemigo()
        if ente is not None:
            ente.enteAtacado(self)
        
    def buscarEnemigo(self):
        pass
    
    def buscarVigilante(self):
        pass
    
    def enteAtacado(self,alguien):
        self.estado.enteAtacado(self,alguien)
    
    def esHeridoPor(self, alguien):
        self.estado.enteEsHeridoPor(self, alguien)
        
    def saMorio (self):
        pass
    
    def loPuedenAtacar(self,alguien):
        print (alguien, "se quiere cargar a", self)
        self.vidas -= int(alguien.poder)
        
        if self.vidas <= 0:
            self.vidas= 0
            self.saMorio()
        
        else:
            print (self, "tiene", self.vidas, "vidas")
