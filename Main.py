
from EM.Cont.Laberinto import Laberinto
from Game.Juego import Juego
from LaberintoFactory import LaberintoFactory


juego= Juego()

#juego.fabricarLaberinto2Habitaciones()
#print(juego)

#juego.fabricarLaberinto2HabitacionesFM()
#print(juego)

#juego.fabricarLaberinto2HabitacionesFMD()
#print(juego)

juego.fabricarLaberinto2Habitaciones2BombasFM()
juego.activarBombas()
print(juego)

#juego.fabricarLaberinto4Habitaciones4BichosFM()
#print(juego)

af= LaberintoFactory()

juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)

print(juego)
