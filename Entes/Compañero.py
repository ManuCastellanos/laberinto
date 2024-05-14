
from colorama import Fore, Style, init
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
        init()
        self.estado= Muerto()
        print(Fore.RED+str(self)+' estiró el ala'+Style.RESET_ALL)
        
    
    def puedeAction(self, personaje):
        return self.modo.action(self,personaje)
    
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    
    def quitarVida(self, daño):
        self.vida-= daño
        
        if self.vida<=0:
            self.saMorio()
    
    def esAura(self):
        return self.modo.esAura()
    
    def esBlitz(self):
        return self.modo.esBlitz()
    
    def __str__(self):
        return "Compañero "+str(self.modo)