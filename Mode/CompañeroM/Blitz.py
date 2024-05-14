from time import sleep

from Mode.ModoCompañero import ModoCompañero


class Blitz(ModoCompañero):
    def __init__(self):
        super().__init__()

        
    def esBlitz(self):
        return True

    def buscarEnemigo(self):
        return self.estado.buscarEnemigo(self)
    
    def actuar(self, unCompi, personaje):
        if personaje.compi == unCompi:
            unCompi.atacar()
    
    def __str__ (self):
        return "Blitz"    