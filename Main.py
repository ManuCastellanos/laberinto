
from EM.Cont.Laberinto import Laberinto
from Game.Juego import Juego



juego= Juego()

juego.fabricarLaberinto2HabitacionesFMD()
juego.activarBombas()


print(juego)

juego.desactivarBombas()

print(juego)