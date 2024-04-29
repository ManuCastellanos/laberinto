from State.Estado import Estado

class Vivo(Estado):
    def actua(self, unEnte):
        unEnte.puedeActuar()
        
    def estaVivo(self):
        return True