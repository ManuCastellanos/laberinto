from colorama import Fore, Style, init
from Mode.ModoCompañero import ModoCompañero

class Aura(ModoCompañero):
    def __init__(self):
        super().__init__()
    
    def esAura(self):
        return True

    def actuar(self, unCompi, personaje):
        init()
        if personaje.compi == unCompi:
            personaje.vidas += 1
            print(Fore.GREEN+"Aura le da 1 de vida a "+str(personaje) + " y ahora tiene "+str(personaje.vidas) + " vidas."+Style.RESET_ALL)
    
    def __str__(self) -> str:
        return "Aura"