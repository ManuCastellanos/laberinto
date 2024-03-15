from EM.Pared.ParedBomba import ParedBomba
from Juego import Juego


class JuegoBombas(Juego):
    def fabricarPared(self):
        return ParedBomba()