from Mode.ModoCompañero import ModoCompañero

class Aura(ModoCompañero):
    def __init__(self):
        super().__init__()
    
    def esAura(self):
        return True

    def actuar(self, unCompi, personaje):
        if personaje.compi == unCompi:
            personaje.vidas += 1
            print("Aura le da 1 de vida a "+str(personaje) + " y ahora tiene "+str(personaje.vidas) + " vidas.")
    
    def __str__(self) -> str:
        return "Aura"