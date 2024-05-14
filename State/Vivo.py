from State.Estado import Estado

class Vivo(Estado):
    def actua(self, unEnte):
        unEnte.puedeActuar()
    
    def enteAtacado(self, unEnte, alguien):
        unEnte.loPuedenAtacar(alguien)
          
    def estaVivo(self):
        return True