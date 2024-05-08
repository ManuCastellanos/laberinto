
from Entes.Ente import Ente
from State.Muerto import Muerto

class Compañero(Ente):
    
    def __init__(self):
        super().__init__()
        self.modo = None
        
    def esCompañero(self):
        return True
    
    def actuaC(self, unCompi,personaje):
       self.modo.actuaC(unCompi,personaje)
    
    def actuar(self, personaje):
        self.modo.actuar(self,personaje)
        
    def estaVivo(self):
        return self.estado.estaVivo()
    
    def saMorio(self):
        self.estado= Muerto()
        print(str(self)+' estiró el ala')
    
    def puedeAction(self, personaje):
        return self.modo.action(self,personaje)
    
    def quitarVida(self, daño):
        self.vida-= daño
        
        if self.vida<=0:
            self.saMorio()
    
    def esAura(self):
        return self.modo.esAura()
    
    def esBlitz(self):
        return self.modo.esBlitz()
    
    def __str__(self):
        return "Compañero "+str(self.modo)+ " en "+str(self.posicion.num)
    