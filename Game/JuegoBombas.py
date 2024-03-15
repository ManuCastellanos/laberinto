from EM.Pare.ParedBomba import ParedBomba
from Game.Juego import Juego


class JuegoBombas(Juego):
    def fabricarPared(self):
        return ParedBomba()