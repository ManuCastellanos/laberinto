from Mode.ModoCompañero import ModoCompañero

class Aura(ModoCompañero):
    def __init__(self):
        super().__init__()
    
    def esAura(self):
        return True

    def actuar(self, unCompi, personaje):
        if personaje.compi == unCompi:
            personaje.vidas += 2
            print("Aura le da 2 de vida a "+str(personaje))
    
    def __str__(self) -> str:
        return "Aura"