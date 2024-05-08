from Mode.ModoCompañero import ModoCompañero

class Aura(ModoCompañero):
    def __init__(self):
        super().__init__()
    
    def esAura(self):
        return True

    def actuar(self, personaje):
        personaje.vida += 2
    
    def __str__(self) -> str:
        return "Aura"