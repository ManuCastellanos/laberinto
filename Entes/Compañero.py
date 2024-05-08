
from Entes.Ente import Ente
from State.Muerto import Muerto

class Compañero(Ente):
    
    def __init__(self):
        super().__init__()
        self.modoCompañero = None
        
    def esCompañero(self):
        return True
    
    def action(self):
       pass
    
    def estaVivo(self):
        return self.estado.estaVivo(self)
    
    def saMorio(self):
        self.estado= Muerto()
        print(str(self)+' estiró el ala')
    
    def puedeAction(self, personaje):
        return self.modocompañero.action(self,personaje)
    
    def quitarVida(self, daño):
        self.vida-= daño
        
        if self.vida<=0:
            self.saMorio()
    
    def irA(self, unaOr):
        unaOr.irA(self)
        
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    def esAura(self):
        return self.modocompañero.esAura()
    
    def esBlitz(self):
        return self.modocompañero.esBlitz()
    
    def __str__(self):
        return "Compañero "+str(self.modoCompañero)+ " en "+str(self.posicion.num)
    